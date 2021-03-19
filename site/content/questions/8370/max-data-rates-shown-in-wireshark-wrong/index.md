+++
type = "question"
title = "Max data rates shown in wireshark wrong?"
description = '''I am sniffing packets(wireless) using AirPcap Nx and notice that the max data rates that Wireshark is showing is only 58.5. I know they are sending and receiving at higher rates than what is shown because we have another system that has a paid sniffer program on it that shows higher rates. Also, our...'''
date = "2012-01-13T07:30:00Z"
lastmod = "2012-01-13T08:32:00Z"
weight = 8370
keywords = [ "wireless", "rates", "speed", "settings" ]
aliases = [ "/questions/8370" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Max data rates shown in wireshark wrong?](/questions/8370/max-data-rates-shown-in-wireshark-wrong)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8370-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am sniffing packets(wireless) using AirPcap Nx and notice that the max data rates that Wireshark is showing is only 58.5. I know they are sending and receiving at higher rates than what is shown because we have another system that has a paid sniffer program on it that shows higher rates. Also, our devices say what they are transmitting at. Is this a limitation in Wireshark, or a setting I need to adjust?</p></div><div id="question-tags" class="tags-container tags">wireless rates speed settings</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Jan '12, 07:30</strong></p><img src="https://secure.gravatar.com/avatar/0f45b0b7c1b00749c4fb6fc9126f61fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joseph%20Conley&#39;s gravatar image" /><p>Joseph Conley<br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joseph Conley has no accepted answers">0%</span></p></div></div><div id="comments-container-8370" class="comments-container"></div><div id="comment-tools-8370" class="comment-tools"></div><div class="clear"></div><div id="comment-8370-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="8372"></span>

<div id="answer-container-8372" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-8372-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Are you using Radiotap encapsulation? If so you might want to try PPI instead. The AirPcap driver conforms to an older version of the Radiotap specification, one which doesn't allow higher data rates to be reported correctly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Jan '12, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p>Gerald Combs ♦♦<br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-8372" class="comments-container"><span id="8374"></span><div id="comment-8374" class="comment"><div id="post-8374-score" class="comment-score"></div><div class="comment-text"><p>PPI is enabled in wireshark? Or an I off target.</p></div><div id="comment-8374-info" class="comment-info"><span class="comment-age">(13 Jan '12, 09:52)</span> Joseph Conley</div></div><span id="8375"></span><div id="comment-8375" class="comment"><div id="post-8375-score" class="comment-score"></div><div class="comment-text"><p>You should be able to set the encapsulation in Wireshark via "Capture→Options→Wireless Settings→Capture Type" or in the AirPcap control panel via "Settings→Capture Type".</p></div><div id="comment-8375-info" class="comment-info"><span class="comment-age">(13 Jan '12, 10:02)</span> Gerald Combs ♦♦</div></div><span id="8376"></span><div id="comment-8376" class="comment"><div id="post-8376-score" class="comment-score"></div><div class="comment-text"><p>That was it, thanks</p></div><div id="comment-8376-info" class="comment-info"><span class="comment-age">(13 Jan '12, 10:24)</span> Joseph Conley</div></div></div><div id="comment-tools-8372" class="comment-tools"></div><div class="clear"></div><div id="comment-8372-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

