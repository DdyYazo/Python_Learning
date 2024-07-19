class ConverterTemperature:
    MAX_CELCIUS = 100;
    MAX_FARENHEIT = 213;
    
    @classmethod
    def _c_f(cls, celsius):
        if celsius > cls.MAX_CELCIUS:
            raise Exception(f'La temperatura C {celsius} es muy alta')
        return celsius * 9/5 + 32
   
    @classmethod
    def _f_c(cls, farenheit):
        if farenheit > cls.MAX_FARENHEIT:
            raise Exception(f'La temperatura F {farenheit} es muy alta')
        return (farenheit-32)* 5/9
    
if __name__ == '__main__':
    result = ConverterTemperature._c_f(12)
    print(f'{result:.2f}')