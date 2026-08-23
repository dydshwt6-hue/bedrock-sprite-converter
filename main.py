import os
import json
import cv2
from PIL import Image
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup

class SpriteConverter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.video_path = ""

        self.lbl_file = Label(text="لم يتم اختيار فيديو", size_hint_y=None, height=40)
        self.add_widget(self.lbl_file)

        btn_browse = Button(text="اختر فيديو MP4", size_hint_y=None, height=50)
        btn_browse.bind(on_press=self.select_video)
        self.add_widget(btn_browse)

        self.add_widget(Label(text="حدد معدل الفريمات (FPS):", size_hint_y=None, height=30))
        self.txt_fps = TextInput(text="10", multiline=False, input_filter="int", size_hint_y=None, height=40)
        self.add_widget(self.txt_fps)

        self.add_widget(Label(text="مستوى التوهج (Emissive 0-255):", size_hint_y=None, height=30))
        self.txt_emissive = TextInput(text="75", multiline=False, input_filter="int", size_hint_y=None, height=40)
        self.add_widget(self.txt_emissive)

        btn_convert = Button(text="إنشاء صور 6x9 (54 فريم)", size_hint_y=None, height=60)
        btn_convert.bind(on_press=self.process)
        self.add_widget(btn_convert)

    def select_video(self, instance):
        content = BoxLayout(orientation='vertical')
        filechooser = FileChooserListView()
        content.add_widget(filechooser)
        
        btn_box = BoxLayout(size_hint_y=None, height=50, spacing=10)
        btn_select = Button(text="اختر")
        btn_cancel = Button(text="إلغاء")
        btn_box.add_widget(btn_cancel)
        btn_box.add_widget(btn_select)
        content.add_widget(btn_box)
        
        popup = Popup(title="اختر فيديو", content=content, size_hint=(0.9, 0.9))
        
        def on_select(btn):
            if filechooser.selection:
                self.video_path = filechooser.selection[0]
                self.lbl_file.text = os.path.basename(self.video_path)
                popup.dismiss()
        
        def on_cancel(btn):
            popup.dismiss()
        
        btn_select.bind(on_press=on_select)
        btn_cancel.bind(on_press=on_cancel)
        popup.open()

    def process(self, instance):
        if not self.video_path:
            self.lbl_file.text = "خطأ: اختر ملف فيديو أولاً!"
            return

        cols = 6
        rows = 9
        max_frames_per_sheet = cols * rows
        
        target_fps = int(self.txt_fps.text) if self.txt_fps.text else 10
        emissive_val = int(self.txt_emissive.text) if self.txt_emissive.text else 75
        
        out_dir = os.path.dirname(self.video_path)
        base_name = os.path.splitext(os.path.basename(self.video_path))[0]
        
        cap = cv2.VideoCapture(self.video_path)
        orig_fps = cap.get(cv2.CAP_PROP_FPS) or 30
        interval = max(1, int(orig_fps / target_fps))

        all_frames = []
        count = 0
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if count % interval == 0:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                all_frames.append(Image.fromarray(frame_rgb))
            count += 1
        cap.release()

        if not all_frames:
            self.lbl_file.text = "خطأ: تعذر استخراج الفريمات!"
            return

        chunks = [all_frames[i:i + max_frames_per_sheet] for i in range(0, len(all_frames), max_frames_per_sheet)]
        fw, fh = all_frames[0].size

        for part_idx, chunk in enumerate(chunks, start=1):
            sheet_name = f"{base_name}_{part_idx}"
            sheet = Image.new("RGBA", (cols * fw, rows * fh))

            for idx, img in enumerate(chunk):
                r = idx // cols
                c = idx % cols
                sheet.paste(img, (c * fw, r * fh))

            sheet.save(os.path.join(out_dir, f"{sheet_name}.png"))
            
            json_data = {
                "format_version": "1.21.30",
                "minecraft:texture_set": {
                    "color": sheet_name,
                    "metalness_emissive_roughness": [0, emissive_val, 0]
                }
            }
            with open(os.path.join(out_dir, f"{sheet_name}.texture_set.json"), "w") as f:
                json.dump(json_data, f, indent=4)

        self.lbl_file.text = f"تم إنشاء {len(chunks)} صورة بنجاح بـ FPS={target_fps}!"

class BedrockSpriteApp(App):
    def build(self):
        return SpriteConverter()

if __name__ == '__main__':
    BedrockSpriteApp().run()
