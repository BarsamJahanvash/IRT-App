from flet import *

PageWidth = 500
PageHeight = 850
Colors = ["#FFFFFF","#00A9F6","#0166BA"]

def main(page: Page):
    page.fonts = {
        "Mona Sans Regular":"Assets/Fonts/Mona-Sans-RegularNarrow.ttf",
        "Mona Sans Medium":"Mona-Sans-MediumNarrow.ttf",
        "Mona Sans Bold":"Mona-Sans-BoldNarrow.ttf"
    }
    # page.window_title_bar_hidden = True
    page.window_width = PageWidth
    page.window_height = PageHeight
    page.vertical_alignment = MainAxisAlignment.START
    page.horizontal_alignment = CrossAxisAlignment.START
    page.padding = 0
    page.scroll = ScrollMode.ALWAYS
    
    StarterCont = Container(
        # margin=10,
        alignment= alignment.center,
        image_src=r"Assets/Pictures/Damavand-Starter.jpg",
        image_fit=ImageFit.COVER,
        height=713,
        width=500,
        content=(
            Stack(
                controls=[
                    # Divider(height=147,color=colors.TRANSPARENT),
                    Column([Text("Discover",size=80,font_family="Mona Sans Regular")],top=127,left=120),
                    Column([Text("IRAN",size=150,font_family="Mona Sans Bold",weight=FontWeight.BOLD)],top=180,left=56,right=56),
                    
                ],
                # alignment = alignment.center
                # horizontal_alignment=CrossAxisAlignment.CENTER,
                # alignment = MainAxisAlignment.START,
                
            )
        )
    )

    page.add(StarterCont)
    page.update()

app(target=main,assets_dir="Assets/")
