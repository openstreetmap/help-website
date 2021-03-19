+++
type = "question"
title = "Wireless IP traffic using AirPcap"
description = '''Hi  My name is Satwik and I have a AirPcap adapter with me. I currently need to examine few Wireless IP packets and observe their QOS values. I have installed my AIRPCAP adapter andwhile running wireshark it seems to show only beacon frames. Somehow I dont see any actual data packets(say RTP packets...'''
date = "2013-06-25T06:56:00Z"
lastmod = "2013-06-25T16:32:00Z"
weight = 22323
keywords = [ "wireless", "airpcap", "qos", "wireshark" ]
aliases = [ "/questions/22323" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Wireless IP traffic using AirPcap](/questions/22323/wireless-ip-traffic-using-airpcap)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22323-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22323-score" class="post-score" title="current number of votes">0</div><span id="post-22323-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi My name is Satwik and I have a AirPcap adapter with me. I currently need to examine few Wireless IP packets and observe their QOS values. I have installed my AIRPCAP adapter andwhile running wireshark it seems to show only beacon frames. Somehow I dont see any actual data packets(say RTP packets/SIP signalling packets). I contacted the Riverbed support team(AirPcap) and they said the hardware has nothing to do with it. Is there a specific Wireshark version I need to use to make this work.Or is there a specific setting I need to make ? Suggestions would be helpful</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-wireless" rel="tag" title="see questions tagged &#39;wireless&#39;">wireless</span> <span class="post-tag tag-link-airpcap" rel="tag" title="see questions tagged &#39;airpcap&#39;">airpcap</span> <span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Jun '13, 06:56</strong></p><img src="https://secure.gravatar.com/avatar/b6d5b52f550b67842071882e0cc34e96?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Satwik&#39;s gravatar image" /><p><span>Satwik</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Satwik has no accepted answers">0%</span></p></div></div><div id="comments-container-22323" class="comments-container"><span id="22326"></span><div id="comment-22326" class="comment"><div id="post-22326-score" class="comment-score"></div><div class="comment-text"><p>are you capturing on the correct channel on your WiFi and do you have the correct AirPcap Adapter for your wireless technology? Do you use 802.11a/b/g or n?</p></div><div id="comment-22326-info" class="comment-info"><span class="comment-age">(25 Jun '13, 08:01)</span> <span class="comment-user userinfo">Landi</span></div></div><span id="22329"></span><div id="comment-22329" class="comment"><div id="post-22329-score" class="comment-score"></div><div class="comment-text"><p>Hi I am currently listening on 802.11 b/g on channel 6 and I checkd the same on the AP side too. Does the presence of beacon frames gurantee that I am listening in the right channel ? Is there something else I need to check ? Thansk and regards Satwik</p></div><div id="comment-22329-info" class="comment-info"><span class="comment-age">(25 Jun '13, 08:27)</span> <span class="comment-user userinfo">Satwik</span></div></div><span id="22332"></span><div id="comment-22332" class="comment"><div id="post-22332-score" class="comment-score"></div><div class="comment-text"><p>You have to see the beacon frames coming from the associated AP where you want to capture from. If you see those and don't have channel hopping but really using a fixed frequency you should be good</p></div><div id="comment-22332-info" class="comment-info"><span class="comment-age">(25 Jun '13, 08:38)</span> <span class="comment-user userinfo">Landi</span></div></div></div><div id="comment-tools-22323" class="comment-tools"></div><div class="clear"></div><div id="comment-22323-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="22334"></span>

<div id="answer-container-22334" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22334-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22334-score" class="post-score" title="current number of votes">0</div><span id="post-22334-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><blockquote><p>Or is there a specific setting I need to make ?</p></blockquote><p>If this is a protected network (WEP or WPA/WPA2), you'll need to tell it the password for the network (and, for WPA/WPA2, will have to see the EAPOL exchange when the machine whose traffic you're trying to see joins the network).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Jun '13, 16:02</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-22334" class="comments-container"><span id="22335"></span><div id="comment-22335" class="comment"><div id="post-22335-score" class="comment-score"></div><div class="comment-text"><p>Hi I somehow got it working.Dont know how it started working though.I will try to figure out the root cause and post it here.(Just in case it turns out to be useful to someone else)</p></div><div id="comment-22335-info" class="comment-info"><span class="comment-age">(25 Jun '13, 16:32)</span> <span class="comment-user userinfo">Satwik</span></div></div></div><div id="comment-tools-22334" class="comment-tools"></div><div class="clear"></div><div id="comment-22334-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

