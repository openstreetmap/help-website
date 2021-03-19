+++
type = "question"
title = "Is there a way to quickly get back to the previous filter after viewing TCP stream?"
description = '''I analyze pcaps and their TCP streams, almost daily. I apply my specific HTTP filter, sort them according to DNS names and then follow TCP stream for specific packet. But when I follow TCP stream of a packet, then wireshark applies another filter for this. When I close the TCP stream window then I g...'''
date = "2015-03-04T03:11:00Z"
lastmod = "2015-03-08T05:00:00Z"
weight = 40251
keywords = [ "filter", "tcp.stream", "display-filter", "wireshark" ]
aliases = [ "/questions/40251" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Is there a way to quickly get back to the previous filter after viewing TCP stream?](/questions/40251/is-there-a-way-to-quickly-get-back-to-the-previous-filter-after-viewing-tcp-stream)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40251-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I analyze pcaps and their TCP streams, almost daily.</p><p>I apply my specific HTTP filter, sort them according to DNS names and then follow TCP stream for specific packet. But when I follow TCP stream of a packet, then wireshark applies another filter for this. When I close the TCP stream window then I get that TCP stream applied as my filter, and not my original filter.</p><p>To go back to my main filter, I have to scroll down or re-type(because the list only saves few recent filters, which get occupied by my followed TCP streams) the filter after each TCP stream. I have to repeat it again and again, which is very inconvenient and time consuming.</p><p>In the tool bar there is no back button that will take me to the filter I was viewing before the TCP stream, ideally there should be something like that, but I could not find any method.</p><p>So, is there a way to achieve it? If not then can I suggest wireshark to add such feature, because it'll be really helpful for those who are facing similar issue.</p><p>Wireskare version: 1.6.7 OS: Ubuntu 12.04 LTS</p></div><div id="question-tags" class="tags-container tags">filter tcp.stream display-filter wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Mar '15, 03:11</strong></p><img src="https://secure.gravatar.com/avatar/e3551fcc25933cc9cd54c8f336774ee7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="muntaha&#39;s gravatar image" /><p>muntaha<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="muntaha has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 04 Mar '15, 03:16</p></div></div><div id="comments-container-40251" class="comments-container"></div><div id="comment-tools-40251" class="comment-tools"></div><div class="clear"></div><div id="comment-40251-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="40252"></span>

<div id="answer-container-40252" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40252-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think there is a faster way of doing this with the Wireshark GUI. You could increase the recent filters in the drop down menu in the Preferences (in the "User Interface" section, there is a field for "Maximum recent filters"). Or you could go to the <a href="http://bugs.wireshark.org">bug tracker</a> and add a feature request for a "back button" like you described.</p><p>But maybe you should also look at non-GUI tools, e.g. scripting your tasks with tshark to extract certain things in a batch, and/or <a href="https://github.com/simsong/tcpflow">tcpflow</a> to display similar content like the "follow TCP stream" feature.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>04 Mar '15, 03:23</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div></div><div id="comments-container-40252" class="comments-container"><span id="40253"></span><div id="comment-40253" class="comment"><div id="post-40253-score" class="comment-score">1</div><div class="comment-text"><p>Also note that if such a change was made, then it's likely to only be in the next version (1.99.x or 2.0.x), as we only back port bug fixes to the current (1.12.x) and previous (1.10.x) versions, so folks using a distro package such as that in Ubuntu 12.04 won't see these changes at all unless they install an up to date package from elsewhere that will probably have all other sorts of dependencies that 12.04 doesn't support.</p></div><div id="comment-40253-info" class="comment-info"><span class="comment-age">(04 Mar '15, 03:32)</span> grahamb ♦</div></div></div><div id="comment-tools-40252" class="comment-tools"></div><div class="clear"></div><div id="comment-40252-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40283"></span>

<div id="answer-container-40283" class="answer answered-by-owner">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40283-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Following is a workaround to get back to my main sorted http filter. It'll only work in the simple filter case and not in the complex cases:<br />
When you are in TCP stream filter then click on button <strong>'clear'</strong>. It has functionality 'clear this filter string and update the display'. You'll find this button in the row of filter field. It'll clear the tcp stream filter and take you back to sorted http stream.</p><p>Wireskare version: 1.6.7<br />
OS: Ubuntu 12.04 LTS</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>05 Mar '15, 06:01</strong></p><img src="https://secure.gravatar.com/avatar/e3551fcc25933cc9cd54c8f336774ee7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="muntaha&#39;s gravatar image" /><p>muntaha<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="muntaha has no accepted answers">0%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p>edited 05 Mar '15, 06:41</p></div></div><div id="comments-container-40283" class="comments-container"><span id="40285"></span><div id="comment-40285" class="comment"><div id="post-40285-score" class="comment-score">1</div><div class="comment-text"><p>not here, for me it just clears the filter completely. It does not go back to any previous filter automatically, on Wireshark 1.12.4.</p></div><div id="comment-40285-info" class="comment-info"><span class="comment-age">(05 Mar '15, 06:15)</span> Jasper ♦♦</div></div><span id="40287"></span><div id="comment-40287" class="comment"><div id="post-40287-score" class="comment-score"></div><div class="comment-text"><p>@Jasper, thanks for observing it. I just rechecked the process, your observation is correct. Its the same scenario on wireshark 1.6.7 too. The result of 'clear' seemed to be my old filter because the packets were in sorted order, and filter was simple 'http'. After removing the tcp stream, I went back to the same packet and same sorted list. So, I have not found solution but a workaround for at least my requirements.</p></div><div id="comment-40287-info" class="comment-info"><span class="comment-age">(05 Mar '15, 06:35)</span> muntaha</div></div><span id="40288"></span><div id="comment-40288" class="comment"><div id="post-40288-score" class="comment-score"></div><div class="comment-text"><p>Going to update this Q/A thread accordingly. Changed this answer from "solution" to "workaround".</p></div><div id="comment-40288-info" class="comment-info"><span class="comment-age">(05 Mar '15, 06:37)</span> muntaha</div></div></div><div id="comment-tools-40283" class="comment-tools"></div><div class="clear"></div><div id="comment-40283-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="40363"></span>

<div id="answer-container-40363" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-40363-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>One other workaround is to use the "Save" button to save the current filter, it will create a new button on the display filter bar. This new button will apply the display filter that was used when the button was created. So after each "follow TCP stream" action, you can then press the new button.</p><p>To remove the button, you need to go to "Edit -&gt; Preferences -&gt; Filter Expressions".</p><p>(not sure though if the "Save" option was already available in 1.6.x)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>08 Mar '15, 05:00</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40363" class="comments-container"></div><div id="comment-tools-40363" class="comment-tools"></div><div class="clear"></div><div id="comment-40363-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

