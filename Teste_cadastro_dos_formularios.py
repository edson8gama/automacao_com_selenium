from sampleTricentisCadastro import SampleTricentisCadastro
from FormVehicleData import FrmVehicleData
from FormInsurantData import FrmInsurantData
from FormProductData import FrmProductData
from FormPriceOption import FrmPriceOption
from FormQuote import FrmQuote
from time import sleep

tempinms = 0.5


def frm_vehicle_data_teste(form):
    form.make('Renault')
    sleep(tempinms)

    form.engineperformance('200')
    sleep(tempinms)

    form.dateofmanufacture('01/01/2010')
    sleep(tempinms)

    form.numberofseats('5')
    sleep(tempinms)

    form.fuel('Other')
    sleep(tempinms)

    form.listprice('20000')
    sleep(tempinms)

    form.annualmileage('400')
    sleep(tempinms)

    form.nextenterinsurantdata()
    sleep(tempinms)


def frm_insurant_data_teste(form):
    form.firstname('Edson')
    sleep(tempinms)

    form.lastname('Gama')
    sleep(tempinms)

    form.birthdate('05/23/1987')
    sleep(tempinms)

    form.gender(1)
    sleep(tempinms)

    form.country('Brazil')
    sleep(tempinms)

    form.zipcode('07179')
    sleep(tempinms)

    form.occupation('Unemployed')
    sleep(tempinms)

    form.hobbies(5)
    sleep(tempinms)

    form.nextenterproductdata()
    sleep(tempinms)


def frm_product_data_teste(form):
    form.startdate('01/01/2021')
    sleep(tempinms)

    form.insurancesum(2)
    sleep(tempinms)

    form.merit_rating('Bonus 1')
    sleep(tempinms)

    form.damage_insurance('Full Coverage')
    sleep(tempinms)

    form.optional_products(2)
    sleep(tempinms)

    form.courtsy_car(3)
    sleep(tempinms)

    form.nextselectpriceoption()
    sleep(tempinms)


def frm_price_option_teste(form):
    form.cod(1)
    sleep(tempinms)

    form.nextsendquote()
    sleep(tempinms)


def frm_quote_teste(form):
    form.email('edson.richard@gmail.com')
    sleep(tempinms)

    form.phone('5511966550912')
    sleep(tempinms)

    form.username('edson')
    sleep(tempinms)

    form.password('Edsonedson1')
    sleep(tempinms)

    form.confirm_password('Edsonedson1')
    sleep(tempinms)

    form.send_email()
    sleep(tempinms)

    form.confirm()
    sleep(tempinms)


if __name__ == '__main__':
    teste = SampleTricentisCadastro()
    teste.start()
    teste.resolucao()

    frm = FrmVehicleData(teste)
    frm_vehicle_data_teste(frm)

    frm = FrmInsurantData(teste)
    frm_insurant_data_teste(frm)

    frm = FrmProductData(teste)
    frm_product_data_teste(frm)

    frm = FrmPriceOption(teste)
    frm_price_option_teste(frm)

    frm = FrmQuote(teste)
    frm_quote_teste(frm)

    teste.driver.close()
    teste.driver.quit()
