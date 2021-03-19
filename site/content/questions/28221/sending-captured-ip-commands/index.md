+++
type = "question"
title = "Sending Captured IP Commands"
description = '''Hi Guys, I am trying to figure out the commands that various AV devices use to perform functions (volume up, down, mute.) etc. so I can put them in another app (not from the manufacturer) and combine to control lots of devices from one app. I have so far captured the dump and found AAAAAQAAAAEAAAAUA...'''
date = "2013-12-17T11:59:00Z"
lastmod = "2013-12-18T04:33:00Z"
weight = 28221
keywords = [ "tv", "capture", "command" ]
aliases = [ "/questions/28221" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Sending Captured IP Commands](/questions/28221/sending-captured-ip-commands)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28221-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Guys,</p><p>I am trying to figure out the commands that various AV devices use to perform functions (volume up, down, mute.) etc. so I can put them in another app (not from the manufacturer) and combine to control lots of devices from one app.</p><p>I have so far captured the dump and found AAAAAQAAAAEAAAAUAw== means mute, but there is a bit more involved like the HTTP PORT command.</p><p>I am just learning wireshark, as in my 15 years IT career I have never needed it, but I learn quick so any help would be greatly appreciated.</p><p>Can anyone tell me how to look at the capture and then send it back to the TV from another program (like telnet or Hercules) so I can test the command is working and figure out if I need to send anything else.</p><p>You can grab the file from <a href="https://www.dropbox.com/s/4f7eno1bciebpxr/Sony%20Sideview%20to%2055%20W805%20TV-%20mute%20command.pcapng">https://www.dropbox.com/s/4f7eno1bciebpxr/Sony%20Sideview%20to%2055%20W805%20TV-%20mute%20command.pcapng</a></p><p>Look forward to any help anyone can give me.</p><p>Thanks</p><p>Minesh</p></div><div id="question-tags" class="tags-container tags">tv capture command</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>17 Dec '13, 11:59</strong></p><img src="https://secure.gravatar.com/avatar/17a0b06a6635de5ce2ed13583d5323c3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MineshT&#39;s gravatar image" /><p>MineshT<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MineshT has no accepted answers">0%</span></p></div></div><div id="comments-container-28221" class="comments-container"><span id="34280"></span><div id="comment-34280" class="comment"><div id="post-34280-score" class="comment-score"></div><div class="comment-text"><p>Did you make any progress? I would like to do a volume control for HAI for myself, not commercially. I'm an amateur, so would appreciate any references to converting Wireshark captures into network commands.</p></div><div id="comment-34280-info" class="comment-info"><span class="comment-age">(29 Jun '14, 19:13)</span> MikeD</div></div></div><div id="comment-tools-28221" class="comment-tools"></div><div class="clear"></div><div id="comment-28221-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="28236"></span>

<div id="answer-container-28236" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28236-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I think it is a bit more complicated than using TelNet or Hercules, because you need to send XML statements via HTTP POST which includes a cookie. I have no idea if the cookie is mandatory and needs to be agreed upon before being able to send commands, but I guess you'll have to either write a small program that can send your specific XML statements via HTTP POST command, or you play around with tools like <a href="http://curl.haxx.se/">curl</a> to mimic the behavior.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '13, 00:17</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-28236" class="comments-container"></div><div id="comment-tools-28236" class="comment-tools"></div><div class="clear"></div><div id="comment-28236-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="28253"></span>

<div id="answer-container-28253" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-28253-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Why reverse engineer something, if there are ready to use tools ;-))</p><blockquote><p><a href="https://github.com/ryanvz/sony_remote">https://github.com/ryanvz/sony_remote</a></p></blockquote><p>They use a similar 'API' that can be found in your capture file, so I guess it will help you to understand and mimic the whole thing better than by just looking at the capture files.</p><p>It does not contain the commands for volume up, down, etc. but as far as I could see, you can request the available commands from the device (your TV) with the method load_commands() in that Ruby library. Maybe that works on your TV as well...</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>18 Dec '13, 04:33</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div></div><div id="comments-container-28253" class="comments-container"></div><div id="comment-tools-28253" class="comment-tools"></div><div class="clear"></div><div id="comment-28253-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

