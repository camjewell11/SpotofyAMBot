const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
    if (msg.content === 'ping') {
        msg.reply('pong');
    }
});

client.login('OTAwMDk5NDEwODE2NTQ4OTc1.YW8Y5g.tzagKKNhmoesKkHB74F0hlvArKk');