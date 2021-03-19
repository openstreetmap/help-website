+++
type = "question"
title = "Auto start Wireshark with a filter"
description = '''Hey, im having issues to start wireshark with the filter i need. I can auto start capturing from the Interface i need. using the -i # and -k   but i cant set the followint filter to be started aswell currently: expert.message contains &quot;GET /bahamut_n/top/&quot; only that filter has the info that im alway...'''
date = "2013-06-29T05:39:00Z"
lastmod = "2013-06-29T07:05:00Z"
weight = 22466
keywords = [ "filter", "capture", "automatically" ]
aliases = [ "/questions/22466" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Auto start Wireshark with a filter](/questions/22466/auto-start-wireshark-with-a-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22466-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>im having issues to start wireshark with the filter i need.</p><p>I can auto start capturing from the Interface i need. using the -i # and -k<br />
</p><p>but i cant set the followint filter to be started aswell currently: expert.message contains "GET /bahamut_n/top/"</p><p>only that filter has the info that im always looking for - so all the other info that goes back and forth with the server is useless for me so id rather only see that info - not the whole IP stuff.</p><p>Any help is highly appreciated.</p><p>Ryuu</p></div><div id="question-tags" class="tags-container tags">filter capture automatically</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>29 Jun '13, 05:39</strong></p><img src="https://secure.gravatar.com/avatar/364ef583850380255feb099eeda67925?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ryuuske01&#39;s gravatar image" /><p>Ryuuske01<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ryuuske01 has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-22466" class="comments-container"></div><div id="comment-tools-22466" class="comment-tools"></div><div class="clear"></div><div id="comment-22466-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22468"></span>

<div id="answer-container-22468" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-22468-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The filter you mention is a display filter, so even if you apply that at start of Wireshark you will still capture everything else. To exclude frames on capture you need to create a capture filter, and that will be quite complicated in your case (if possible at all), because it will probably have to filter on specific offsets to look for that message). You should familiarize yourself with the difference between capture and display filters and how to create capture filters.</p><p>There are some examples on this Wiki page that might help you: <a href="http://wiki.wireshark.org/CaptureFilters">http://wiki.wireshark.org/CaptureFilters</a></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '13, 07:05</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 29 Jun '13, 07:07</p></div></div><div id="comments-container-22468" class="comments-container"><span id="22469"></span><div id="comment-22469" class="comment"><div id="post-22469-score" class="comment-score"></div><div class="comment-text"><p>Yes i know :)</p><p>the thing is i dont really need the capture filter - it can capture all data while i work with that display filter. since i really need it just for 1-2 minutes and then i reset wireshark anyway to get the new info in the same display filter.</p><p>is it possible to set the display filter to also auto-start?</p></div><div id="comment-22469-info" class="comment-info"><span class="comment-age">(29 Jun '13, 07:13)</span> Ryuuske01</div></div><span id="22472"></span><div id="comment-22472" class="comment"><div id="post-22472-score" class="comment-score"></div><div class="comment-text"><p>Yes. Try</p><p>Wireshark -Y "Display Filter"</p><p>You can find all parameters Wireshark accepts by starting it from the command line with the -h parameter.</p></div><div id="comment-22472-info" class="comment-info"><span class="comment-age">(29 Jun '13, 11:10)</span> Jasper ♦♦</div></div></div><div id="comment-tools-22468" class="comment-tools"></div><div class="clear"></div><div id="comment-22468-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

