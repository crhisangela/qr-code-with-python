# QR code com python

Para criar o QR code é usada a biblioteca **qrcode**.

No field "data" você pode mudar para a frase ou link que desejar gerar o QRCode.

De maneira simplificada para gerar um QRCode basta apenas usar o comando ``qrcode.make([TEXTO OU LINK DESEJADO])`` mas no código deixei um pouco estilizado, oq ue pode ser alterado para a maneira que quiser.

Caso você deseje criar diversos QRCodes de diversos textos/links diferentes, isso seria facilmente resolvido com um Loop de qrcode.make(data) e data.save.

image.png

By: **sıɥɹƆ sıɥɹƆ**