+++
type = "question"
title = "capture filter,  syntax error in filter string, wireshark 1.8.2"
description = '''i upgraded to wirshark 1.8.0 , could not get a filter to work , syntex error in filter string . i upgraded to wireshark 1.8.2 , still the same problem . tried two filters  filter name = IP address 192.168.0.1 filter string = host 192.168.0.1  filter name = test ip address filter string = ! ( ip.addr...'''
date = "2012-09-19T09:16:00Z"
lastmod = "2012-09-19T10:07:00Z"
weight = 14380
keywords = [ "capture-filter", "display-filter" ]
aliases = [ "/questions/14380" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [capture filter, syntax error in filter string, wireshark 1.8.2](/questions/14380/capture-filter-syntax-error-in-filter-string-wireshark-182)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14380-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>i upgraded to wirshark 1.8.0 , could not get a filter to work , syntex error in filter string . i upgraded to wireshark 1.8.2 , still the same problem . tried two filters filter name = IP address 192.168.0.1 filter string = host 192.168.0.1</p><p>filter name = test ip address filter string = ! ( ip.addr == 10.43.54.65 )</p><p>each has a error Invalid capture filter "test ip address" for interface Intel(R) 82579LM Gigabit Network Connection: \Device\NPF_{D9470C12-7560-4669-AA38-CC092A8EA807}!</p><p>That string isn't a valid capture filter (syntax error). See the User's Guide for a description of the capture filter syntax.</p></div><div id="question-tags" class="tags-container tags">capture-filter display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>19 Sep '12, 09:16</strong></p><img src="https://secure.gravatar.com/avatar/e7cb49ed5265dcd4c2fa5de8092be9b9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mwillenb&#39;s gravatar image" /><p>mwillenb<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mwillenb has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 19 Sep '12, 10:08</p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span></p></div></div><div id="comments-container-14380" class="comments-container"><span id="14381"></span><div id="comment-14381" class="comment"><div id="post-14381-score" class="comment-score"></div><div class="comment-text"><p>i even used one of the sample filters that was loaded in the install filter name = IP address 192.168.0.1 filter string = host 192.168.0.1</p></div><div id="comment-14381-info" class="comment-info"><span class="comment-age">(19 Sep '12, 09:21)</span> mwillenb</div></div></div><div id="comment-tools-14380" class="comment-tools"></div><div class="clear"></div><div id="comment-14380-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="14382"></span>

<div id="answer-container-14382" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-14382-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p><em>each has a error Invalid capture filter "test ip address" for interface Intel(R) 82579LM Gigabit Network Connection: \Device\NPF_{D9470C12-7560-4669-AA38-CC092A8EA807}!</em></p><p>It appears that you are attempting to use the filter name instead of the filter string. But even if you had correctly used the filter string, it would have still failed in those cases because those are display filters, not capture filters. If you are adding capture filters, then they must be in proper capture filter syntax. A proper filter will cause the background of the filter string field to turn green. <a href="http://www.cs.ucr.edu/~marios/ethereal-tcpdump.pdf">This</a> document may help you with capture filter syntax, or refer to the <a href="http://www.manpagez.com/man/7/pcap-filter/">pcap-filter</a> man page. For IP display filter help, see the Wireshark <a href="http://wiki.wireshark.org/Internet_Protocol">Internet_protocol</a> wiki page.</p><p>Lastly, don't forget about the Wireshark <a href="http://www.wireshark.org/docs/wsug_html_chunked/ChWorkDefineFilterSection.html#FiltersDialog">user guide</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Sep '12, 10:07</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p>cmaynard ♦♦<br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-14382" class="comments-container"><span id="14384"></span><div id="comment-14384" class="comment"><div id="post-14384-score" class="comment-score"></div><div class="comment-text"><p>i got it working , but my complaint is still valid ,<br />
if i only select the CAPTURE pull down menu and CLICK the CAPTURE FILTER on the menu bar i get a new window " Wireshark Capture Filter - Profile Default. try to creat a filter profile<br />
filter name test ip address filter string ip addr == 216.69.108.117<br />
</p><p>then i duble click the interface , to get the " Edit Iterface Settings " screen and try to fill in the Capture Filter: by picking the filter ,<br />
the field fills in with ip addr == 216.69.108.117 i start the capture and get the bad syntex error .</p><p>but i set the capture filter profile anf the edit interface setting back to default . then i add to the Filter field ip.addr == 216.69.108.117 and start the capture this set up works so i will do this for a capture filter .</p><p>i will ignore the " Wireshark Capture Filter Profiler " and the " edit interface settings / capture filter field "</p></div><div id="comment-14384-info" class="comment-info"><span class="comment-age">(19 Sep '12, 11:38)</span> mwillenb</div></div><span id="14385"></span><div id="comment-14385" class="comment"><div id="post-14385-score" class="comment-score"></div><div class="comment-text"><p>in the previous letter , i did use<br />
</p><p>ip.addr == 216.69.108.117</p><p>the</p><p>ip addr == 216.69.108.117 was a typo</p></div><div id="comment-14385-info" class="comment-info"><span class="comment-age">(19 Sep '12, 11:40)</span> mwillenb</div></div><span id="14386"></span><div id="comment-14386" class="comment"><div id="post-14386-score" class="comment-score"></div><div class="comment-text"><p>"<code>ip.addr == 216.69.108.117</code>" is a display filter, not a capture filter. That's why it fails. Review display filters vs. capture filters for proper syntax. In this particular case though, the capture filter you want is "<code>ip host 216.69.108.117</code>".</p></div><div id="comment-14386-info" class="comment-info"><span class="comment-age">(19 Sep '12, 11:46)</span> cmaynard ♦♦</div></div></div><div id="comment-tools-14382" class="comment-tools"></div><div class="clear"></div><div id="comment-14382-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

