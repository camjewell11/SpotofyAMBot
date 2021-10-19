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

bot.on('message', (message) => { //whenever a message is sent
    if (message.content.includes('music.apple.com')) { //if it contains an AM link
        message.delete() //delete the message
        .then(message.channel.send('Link Deleted:\n**Invite links are not permitted on this server**'))
    }
})

client.login('OTAwMDk5NDEwODE2NTQ4OTc1.YW8Y5g.B3YKYiEvlFUpXLmgfgBlPTld7iN');