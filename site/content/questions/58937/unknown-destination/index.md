+++
type = "question"
title = "unknown destination"
description = '''hi, I have started using wireshark only recently and I have noticed something weird, every time I filter packages by &quot;http&quot; I see that my pc sends the first request to an IP address, which I know belongs to my university and the host is my university&#x27;s website, although I don&#x27;t browse to the univers...'''
date = "2017-01-21T15:34:00Z"
lastmod = "2017-01-22T04:05:00Z"
weight = 58937
keywords = [ "unknown" ]
aliases = [ "/questions/58937" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [unknown destination](/questions/58937/unknown-destination)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58937-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>hi, I have started using wireshark only recently and I have noticed something weird, every time I filter packages by "http" I see that my pc sends the first request to an IP address, which I know belongs to my university and the host is my university's website, although I don't browse to the university's website,and actually I have graduated from that university and moved to a different country, but my laptop was provided by the university when I started there. So could you please explain why does this happen? see the screenshot<img src="https://osqa-ask.wireshark.org/upfiles/h.JPG" alt="alt text" /></p></div><div id="question-tags" class="tags-container tags">unknown</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Jan '17, 15:34</strong></p><img src="https://secure.gravatar.com/avatar/2f95d01b51a61bbb31a0fb670dec5076?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="VP7777&#39;s gravatar image" /><p>VP7777<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="VP7777 has no accepted answers">0%</span></p></img></div></div><div id="comments-container-58937" class="comments-container"></div><div id="comment-tools-58937" class="comment-tools"></div><div class="clear"></div><div id="comment-58937-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="58943"></span>

<div id="answer-container-58943" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-58943-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, probably, some software is still installed on your laptop and is called from autorun.This piece of software can perform automatic connection attempts. It doesn't neccessarily have to be web browser.</p><p>There is 'Perfigo SEC' mentioned in useragent field. Quick searching tells us that could be 'Cisco Clean Access Agent' software.</p><p>You can investigate it further using Sysinternals toolset. TCPView and Procmon utilities can give you process name, and Autoruns utility can show where is it called from.</p><p>Also, next time try to anonymize your screenshot better:) Check 'Full request URI' field - your university's hostname is visible from there too.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Jan '17, 04:05</strong></p><img src="https://secure.gravatar.com/avatar/1e22670f8d643ca08d658b80a6782932?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Packet_vlad&#39;s gravatar image" /><p>Packet_vlad<br />
<span class="score" title="436 reputation points">436</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="13 badges"><span class="bronze">●</span><span class="badgecount">13</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Packet_vlad has 5 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Jan '17, 04:07</p></div></div><div id="comments-container-58943" class="comments-container"><span id="58964"></span><div id="comment-58964" class="comment"><div id="post-58964-score" class="comment-score"></div><div class="comment-text"><p>thanks for the quick reply, I also think it's cisco</p><p>yea, I knew about that hostname for the uni is there) simple google search of the ip would reveal the name so didn't make sense to cut it out, besides not really that big of a secret thanks again</p></div><div id="comment-58964-info" class="comment-info"><span class="comment-age">(23 Jan '17, 01:39)</span> VP7777</div></div><span id="58965"></span><div id="comment-58965" class="comment"><div id="post-58965-score" class="comment-score"></div><div class="comment-text"><p>Your answer has been converted to a comment as that's how this site works. Please read the FAQ for more information.</p></div><div id="comment-58965-info" class="comment-info"><span class="comment-age">(23 Jan '17, 02:14)</span> Jaap ♦</div></div><span id="58966"></span><div id="comment-58966" class="comment"><div id="post-58966-score" class="comment-score"></div><div class="comment-text"><p>If an answer has solved your issue, please accept the answer for the benefit of other users by clicking the checkmark icon next to the answer. Please read the FAQ for more information.</p></div><div id="comment-58966-info" class="comment-info"><span class="comment-age">(23 Jan '17, 02:15)</span> Jaap ♦</div></div></div><div id="comment-tools-58943" class="comment-tools"></div><div class="clear"></div><div id="comment-58943-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

