import flet as ft

def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.update()

    img = ft.Image(
        src=r"/Assets/Pictures/Damavand-Starter.jpg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )
    images = ft.Row(expand=1, wrap=False, scroll="always")

    page.add(img)

    # for i in range(0, 30):
    #     images.controls.append(
    #         ft.Image(
    #             src=f"https://picsum.photos/200/200?{i}",
    #             width=200,
    #             height=200,
    #             fit=ft.ImageFit.NONE,
    #             repeat=ft.ImageRepeat.NO_REPEAT,
    #             border_radius=ft.border_radius.all(10),
    #         )
    #     )
    page.update()

ft.app(target=main,assets_dir="Assets/")