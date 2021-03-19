+++
type = "question"
title = "Access to decrypted WPA/WPA2 data for lua dissector"
description = '''I am using wireshark capturing WLAN traffic with AirPcap. All traffic in WLAN network is always encrypted with WPA/WPA2. So to be able to make analysis I use wireshark to decrypt traffic. Is there way for lua dissector to access this decrypted data ? It seems that some dissector are able to access d...'''
date = "2011-10-07T00:48:00Z"
lastmod = "2011-11-08T20:23:00Z"
weight = 6769
keywords = [ "decryption", "dissector", "lua" ]
aliases = [ "/questions/6769" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Access to decrypted WPA/WPA2 data for lua dissector](/questions/6769/access-to-decrypted-wpawpa2-data-for-lua-dissector)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6769-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6769-score" class="post-score" title="current number of votes">0</div><span id="post-6769-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am using wireshark capturing WLAN traffic with AirPcap. All traffic in WLAN network is always encrypted with WPA/WPA2. So to be able to make analysis I use wireshark to decrypt traffic. Is there way for lua dissector to access this decrypted data ?</p><p>It seems that some dissector are able to access decrypted data since wireshark recognizes for example ARP messages from decrypted traffic. Or is this only possible to dissectors written in c?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-decryption" rel="tag" title="see questions tagged &#39;decryption&#39;">decryption</span> <span class="post-tag tag-link-dissector" rel="tag" title="see questions tagged &#39;dissector&#39;">dissector</span> <span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '11, 00:48</strong></p><img src="https://secure.gravatar.com/avatar/7fa2536626fed9caa96d07083a59f6be?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sio&#39;s gravatar image" /><p><span>Sio</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sio has no accepted answers">0%</span></p></div></div><div id="comments-container-6769" class="comments-container"><span id="6824"></span><div id="comment-6824" class="comment"><div id="post-6824-score" class="comment-score"></div><div class="comment-text"><p>One way to get around this problem could be to output capture with tshark as hex dump, and then use text2pcap to make it again capture file. But this sounds bit too complicated.</p></div><div id="comment-6824-info" class="comment-info"><span class="comment-age">(10 Oct '11, 04:44)</span> <span class="comment-user userinfo">Sio</span></div></div><span id="6831"></span><div id="comment-6831" class="comment"><div id="post-6831-score" class="comment-score"></div><div class="comment-text"><p>OK, I realized I have made newbie error and did not provide enough information. My dissector is <strong>post dissector</strong>. This was because I did not want to restrict dissection to any specific port number. Since protocol I want to dissect uses user configurable port number.</p><p>If I register my dissector as udp dissector, everything works fine and my dissector dissects decrypted data. But as post dissector it does not have access to decrypted data. I am still interested is it possible to make it work as post dissector?</p></div><div id="comment-6831-info" class="comment-info"><span class="comment-age">(10 Oct '11, 06:27)</span> <span class="comment-user userinfo">Sio</span></div></div><span id="7307"></span><div id="comment-7307" class="comment"><div id="post-7307-score" class="comment-score"></div><div class="comment-text"><p>May be you'd provide some source code link to review for possible errors?</p></div><div id="comment-7307-info" class="comment-info"><span class="comment-age">(08 Nov '11, 20:23)</span> <span class="comment-user userinfo">ShomeaX</span></div></div></div><div id="comment-tools-6769" class="comment-tools"></div><div class="clear"></div><div id="comment-6769-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

