+++
type = "question"
title = "Using Rawshark or tshark for wireless traffic"
description = '''Hi ,  I am trying to use AirPcap to sniff wireless packets using t-shark but I cannot save the capture and use a filter together C:&#92;Program Files&#92;Wireshark&amp;gt;tshark.exe -a &quot;duration:5&quot; -R &quot;wlan.fc.type_subtype = = 0x08&quot; -i 1 -w D:tshark.cap  tshark: Read filters aren&#x27;t supported when capturing and ...'''
date = "2012-06-10T23:30:00Z"
lastmod = "2012-06-12T09:23:00Z"
weight = 11804
keywords = [ "rawshark", "beacon", "tshark" ]
aliases = [ "/questions/11804" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Using Rawshark or tshark for wireless traffic](/questions/11804/using-rawshark-or-tshark-for-wireless-traffic)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11804-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11804-score" class="post-score" title="current number of votes">0</div><span id="post-11804-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi ,</p><p>I am trying to use AirPcap to sniff wireless packets using t-shark but I cannot save the capture and use a filter together</p><pre><code>C:\Program Files\Wireshark&gt;tshark.exe -a &quot;duration:5&quot; -R &quot;wlan.fc.type_subtype = = 0x08&quot; -i 1 -w D:tshark.cap

tshark: Read filters aren&#39;t supported when capturing and saving the captured packets.</code></pre><p>So I use t-shark only to capture packets and later try to filter it using rawshark</p><pre><code>C:\Program Files\Wireshark&gt;tshark.exe -a &quot;duration:5&quot; -i 1 -w D:tshark.cap

C:\Program Files\Wireshark&gt;rawshark -R &quot;wlan.fc.type_subtype == 0x08&quot; -d encap:105   -r d:\tshark.cap -s -p  -l</code></pre><p>Unfortunately the output of the command makes no sense. I am trying to sniff beacons but all I get is a set of 0's</p><p>Has anyone tried filtering using tshark or rawshark.</p><p>BTW I am trying tshark because I plan to use it in automation. Pls also suggest any better way to do so if any but by command line</p><p>Regards TroubledUser</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-rawshark" rel="tag" title="see questions tagged &#39;rawshark&#39;">rawshark</span> <span class="post-tag tag-link-beacon" rel="tag" title="see questions tagged &#39;beacon&#39;">beacon</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>10 Jun '12, 23:30</strong></p><img src="https://secure.gravatar.com/avatar/f65b108a904b69735037aa1b6bcdcf57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Trouble%20User&#39;s gravatar image" /><p><span>Trouble User</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Trouble User has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '12, 08:44</strong> </span></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span></p></div></div><div id="comments-container-11804" class="comments-container"><span id="11843"></span><div id="comment-11843" class="comment"><div id="post-11843-score" class="comment-score"></div><div class="comment-text"><p>Hi Fellow techies ,</p><p>Thanks for your replies but it still does not solve my problem .</p><p>I still need to know how to filter packets from the capture file because once I get a capture of beacons , based on my script I may need to filter more paramters . I cannot re-run t-shark because I need a single sample of packets and then run multiple filters on them.</p><p>To quote an example : 1. I get a capture of 500 beacon packets 2. From 500 Beacons I need to check configurations of 4 "SSID" like beacon interval , capability info 3. So I cannot re-run t-shark 4 times because I am doing some changes on the AP and want to capture the info on all 4 SSID simultaneously.</p><p>So your solution on capturing packets holds true if capture needed is only beacons. But here within beacon packets I need 4 Different SSID and their info. I wish to know how to apply a filter to a capture file</p><p>Regards Troubled User</p></div><div id="comment-11843-info" class="comment-info"><span class="comment-age">(11 Jun '12, 19:20)</span> <span class="comment-user userinfo">Trouble User</span></div></div></div><div id="comment-tools-11804" class="comment-tools"></div><div class="clear"></div><div id="comment-11804-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

3 Answers:

</div>

</div>

<span id="11858"></span>

<div id="answer-container-11858" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11858-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11858-score" class="post-score" title="current number of votes">1</div><span id="post-11858-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>So capture your beacons and then filter the capture file:</p><ol><li><code>tshark.exe -a "duration:5" -i 1 -f "type mgt subtype beacon" -w D:tshark.cap</code></li><li><code>tshark -r D:tshark.cap -T fields -e wlan_mgt.ssid -e wlan_mgt.fixed.capabilities</code></li></ol><p>Or if you want to capture packets other than just beacons, then you can apply the display filter to the capture file afterwards:</p><ol><li><code>tshark.exe -a "duration:5" -i 1 -w D:tshark.cap</code></li><li><code>tshark.exe -r D:tshark.cap -R "wlan.fc.type_subtype == 0x08" -T fields -e wlan_mgt.ssid -e wlan_mgt.fixed.capabilities</code></li></ol><p>Refer to the <a href="http://www.wireshark.org/docs/man-pages/tshark.html">tshark man page</a> for more information.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Jun '12, 09:23</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Jun '12, 09:26</strong> </span></p></div></div><div id="comments-container-11858" class="comments-container"></div><div id="comment-tools-11858" class="comment-tools"></div><div class="clear"></div><div id="comment-11858-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11810"></span>

<div id="answer-container-11810" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11810-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11810-score" class="post-score" title="current number of votes">0</div><span id="post-11810-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>If you want to see beacon frames, please try this:</p><blockquote><p><code>tshark -r d:\tshark.cap -R "wlan.fc.type_subtype == 0x08"</code><br />
</p></blockquote><p>The output should look similar to this:</p><blockquote><p><code>1   0.000000 Z-Com_01:02:03 -&gt; Broadcast    802.11 218 Beacon frame, SN=1740, FN=0, Flags=........, BI=200, SSID=WLAN_TEST</code></p></blockquote><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '12, 08:43</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p><span>Kurt Knochner ♦</span><br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></br></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>11 Jun '12, 08:44</strong> </span></p></div></div><div id="comments-container-11810" class="comments-container"></div><div id="comment-tools-11810" class="comment-tools"></div><div class="clear"></div><div id="comment-11810-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="11811"></span>

<div id="answer-container-11811" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-11811-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-11811-score" class="post-score" title="current number of votes">0</div><span id="post-11811-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Try using tshark instead of rawshark, as in:</p><pre><code>`tshark -r d:\tshark.cap -R &quot;wlan.fc.type_subtype == 0x08&quot;`</code></pre><p>Or, if you really only want to capture beacons, you can use a capture filter to do it instead of a display filter. I can't try this command myself at the moment, but this should work:</p><pre><code>tshark.exe -a &quot;duration:5&quot; -i 1 -f &quot;type mgt subtype beacon&quot; -w D:tshark.cap</code></pre><p>Unfortunately, the pcap-filter man page is not yet accessible from <a href="http://www.tcpdump.org/">tcpdump</a>'s website, but you can reference it here instead: <a href="http://www.manpagez.com/man/7/pcap-filter/">http://www.manpagez.com/man/7/pcap-filter/</a>.</p><p>For more helpful filtering tips related to this topic, you might also refer to <a href="http://ask.wireshark.org/users/100/joke">Joke Snelder</a>'s <em><a href="http://www.lovemytool.com/blog/2010/07/wireshark-wireless-display-and-capture-filters-samples-part-2-by-joke-snelders.html">"Wireless Display and Capture Filters Samples"</a></em> article on <a href="http://www.lovemytool.com/">lovemytool</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>11 Jun '12, 08:47</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-11811" class="comments-container"></div><div id="comment-tools-11811" class="comment-tools"></div><div class="clear"></div><div id="comment-11811-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

