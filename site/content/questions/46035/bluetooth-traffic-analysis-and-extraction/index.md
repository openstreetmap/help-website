+++
type = "question"
title = "Bluetooth traffic analysis and extraction"
description = '''Hi, I&#x27;m quite a beginner to Wireshark and got problem using it, I searched the wiki page but seems no promising results. Hopefully I can get some help here. I am trying to analyze the network traffic between LG smart watch and Android phone, which all go through bluetooth channel. Now I have got the...'''
date = "2015-09-21T13:02:00Z"
lastmod = "2015-09-24T14:00:00Z"
weight = 46035
keywords = [ "extraction", "bluetooth", "analysis", "wireshark" ]
aliases = [ "/questions/46035" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Bluetooth traffic analysis and extraction](/questions/46035/bluetooth-traffic-analysis-and-extraction)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46035-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi, I'm quite a beginner to Wireshark and got problem using it, I searched the wiki page but seems no promising results. Hopefully I can get some help here.</p><p>I am trying to analyze the network traffic between LG smart watch and Android phone, which all go through bluetooth channel. Now I have got the network traffic log file and I can view it by running</p><p><strong>&gt; wireshark "LogFileName"</strong></p><p>Problem is how can I retrieve infomation by removing the bluetooth header and get the <strong>original network layer packet</strong>, because I can parse the IP layer packet but bluetooth packet is not what I want and what I understand.</p></div><div id="question-tags" class="tags-container tags">extraction bluetooth analysis wireshark</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Sep '15, 13:02</strong></p><img src="https://secure.gravatar.com/avatar/aea886e707ff247a63ca2d3955533114?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xl45&#39;s gravatar image" /><p>xl45<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xl45 has no accepted answers">0%</span></p></div></div><div id="comments-container-46035" class="comments-container"><span id="46036"></span><div id="comment-46036" class="comment"><div id="post-46036-score" class="comment-score"></div><div class="comment-text"><p>Can you share the Wireshark "log" file? Otherwise it's hard to tell what's wrong with that capture file.</p></div><div id="comment-46036-info" class="comment-info"><span class="comment-age">(21 Sep '15, 13:18)</span> Kurt Knochner ♦</div></div><span id="46037"></span><div id="comment-46037" class="comment"><div id="post-46037-score" class="comment-score"></div><div class="comment-text"><p>Sure, the log file can be accessed here: <a href="https://drive.google.com/file/d/0BxINm19KyB6raTZVZ2lpb2dzZnM/view?usp=sharing">https://drive.google.com/file/d/0BxINm19KyB6raTZVZ2lpb2dzZnM/view?usp=sharing</a></p><p>@Kurt Knochner</p></div><div id="comment-46037-info" class="comment-info"><span class="comment-age">(21 Sep '15, 16:10)</span> xl45</div></div><span id="46038"></span><div id="comment-46038" class="comment"><div id="post-46038-score" class="comment-score"></div><div class="comment-text"><p>actually bluetooth just remove the ethernet header and add its own header with the remaining payload unchanged. but still i have no idea how to do the extraction.</p></div><div id="comment-46038-info" class="comment-info"><span class="comment-age">(21 Sep '15, 16:18)</span> xl45</div></div><span id="46057"></span><div id="comment-46057" class="comment"><div id="post-46057-score" class="comment-score"></div><div class="comment-text"><p>no one knows?</p></div><div id="comment-46057-info" class="comment-info"><span class="comment-age">(22 Sep '15, 09:32)</span> xl45</div></div><span id="46058"></span><div id="comment-46058" class="comment"><div id="post-46058-score" class="comment-score"></div><div class="comment-text"><p>I don't see any IP traffic "encapsulated in Bluetooth" in that capture file.</p><blockquote><p>I am trying to analyze the <strong>network traffic</strong> between LG smart watch and Android phone</p></blockquote><p>Why do you think this is an IP communication?</p></div><div id="comment-46058-info" class="comment-info"><span class="comment-age">(22 Sep '15, 09:48)</span> Kurt Knochner ♦</div></div><span id="46059"></span><div id="comment-46059" class="comment not_top_scorer"><div id="post-46059-score" class="comment-score"></div><div class="comment-text"><p>thanks for answering, well actually i may misunderstand this by thinking that bluetooth just remove ethernet header upon the regular TCP/IP packet and add its own header. but still i have no idea what to do if i want to retrieve data from the packet. @Kurt Knochner</p></div><div id="comment-46059-info" class="comment-info"><span class="comment-age">(22 Sep '15, 10:14)</span> xl45</div></div></div><div id="comment-tools-46035" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-46035-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="46062"></span>

<div id="answer-container-46062" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46062-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>but still i have no idea what to do if i want to retrieve data from the packet.</p></blockquote><p>it depends on the content you are interested in. If I look at the payload of large RFCOMM frames, I can see payload that's seems to be related to smart watch communication.</p><p>So, first you probably need to develop a better understanding of what your are actually looking for, then you can either extract that information manually via the Wireshark GUI (RFCOMM frames), or by using tshark. If you are looking for TCP/IP commuincation between the devices, I don't think there is any in that capture file.</p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>22 Sep '15, 10:59</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 22 Sep '15, 11:00</p></div></div><div id="comments-container-46062" class="comments-container"></div><div id="comment-tools-46062" class="comment-tools"></div><div class="clear"></div><div id="comment-46062-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="46126"></span>

<div id="answer-container-46126" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-46126-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>The RFCOMM service has UUID128: 5e8945b0-9525-11e3-a5e2-0800200c9a66 and name: WearableBt, so I hope it is Android Wear (I hear you can use androiddump in latest Wireshark to live-capturing). As I remember Wear require closed-sources application from Google on Android to make it works (this one: <a href="https://play.google.com/store/apps/details?id=com.google.android.wearable.app&amp;hl=en">https://play.google.com/store/apps/details?id=com.google.android.wearable.app&amp;hl=en</a> ), so there is no any documentation about protocol used by Google to communicate with Wear (implies no easy support for that in Wireshark). If anyone found some documentation about it, please share with me.</p><p>For now... Only Google know how to read Wear payload (over RFCOMM). I think I can see some structures, but it is (not!) reverse engineering.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>24 Sep '15, 14:00</strong></p><img src="https://secure.gravatar.com/avatar/6eabf35b1168a8242bb2d69db18a8a7c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Micha%C5%82%20%C5%81ab%C4%99dzki&#39;s gravatar image" /><p>Michał Łabędzki<br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Michał Łabędzki has one accepted answer">8%</span></p></div></div><div id="comments-container-46126" class="comments-container"></div><div id="comment-tools-46126" class="comment-tools"></div><div class="clear"></div><div id="comment-46126-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

