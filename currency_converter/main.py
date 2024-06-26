import flet as ft
import dictionarys
import CurrencyConverter

def main(page: ft.Page):
    def onGetResult(event):
        result.value="loading ..."
        getResult.disabled=True
        page.update()
        Result=CurrencyConverter.convert(From.value,To.value,float(value.value))
        result.value=str(Result)
        result.focus()
        getResult.disabled=False
        page.update()
    page.title="Currency converter"
    currencies=[]
    for Key ,value in dictionarys.currencies.items():
        currencies.append(ft.dropdown.Option(Key,value))
    From=ft.Dropdown(label="from",options=currencies)
    To=ft.Dropdown(label="to",options=currencies)
    value=ft.TextField(label="value",keyboard_type=ft.KeyboardType.NUMBER,value="1")
    getResult=ft.ElevatedButton(text="get result",on_click=onGetResult)
    result=ft.TextField(label="result",read_only=True)
    page.add(From,To,value,getResult,result)


ft.app(main)
