+++
type = "question"
title = "How to decrypt ssl traffic with tshark 1.6?"
description = '''With previous versions (1.4.x) of tshark I&#x27;ve used the ssl.key_list option, in the following way: tshark.exe -r input.pcap -o ssl.keys_list:172.30.2.107,443,http,private.key -R &quot;http.request&quot; -T fields -e frame.number -e &quot;tcp.stream&quot;  But this seems to no longer work, probably because with new versi...'''
date = "2011-06-27T06:51:00Z"
lastmod = "2015-09-07T00:30:00Z"
weight = 4766
keywords = [ "ssl", "tshark" ]
aliases = [ "/questions/4766" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to decrypt ssl traffic with tshark 1.6?](/questions/4766/how-to-decrypt-ssl-traffic-with-tshark-16)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4766-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4766-score" class="post-score" title="current number of votes">2</div><span id="post-4766-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>With previous versions (1.4.x) of tshark I've used the ssl.key_list option, in the following way:</p><pre><code>tshark.exe -r input.pcap -o ssl.keys_list:172.30.2.107,443,http,private.key  -R &quot;http.request&quot; -T fields -e frame.number -e &quot;tcp.stream&quot;</code></pre><p>But this seems to no longer work, probably because with new versions of wireshark, ssl keys are specified in a file of their own and not under the preferences file. So how should I specify the ssl keys for tshark in 1.6? Must I edit the ssl config file? Is it a bug?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>27 Jun '11, 06:51</strong></p><img src="https://secure.gravatar.com/avatar/9b7b5e633f7836289c2fc6c3934bffaf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="r0u1i&#39;s gravatar image" /><p><span>r0u1i</span><br />
<span class="score" title="61 reputation points">61</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="r0u1i has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>27 Jun '11, 06:51</strong> </span></p></div></div><div id="comments-container-4766" class="comments-container"></div><div id="comment-tools-4766" class="comment-tools"></div><div class="clear"></div><div id="comment-4766-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="5878"></span>

<div id="answer-container-5878" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-5878-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-5878-score" class="post-score" title="current number of votes">1</div><span id="post-5878-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="r0u1i has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>New version Wireshark(v1.6x) put the ssl.key_list to a file named ssl_keys which is in personal profile folder, copy the string and paste under the "-o ssl.keys_list:" option, the difference between the new version and old version is the "ssl.key_list" option format, new version should use UAT string, following is a command line which works for me.</p><p>tshark -r private_bob.pcap -o ssl.keys_list:"192.168.3.206","443","http","e:\education\ssl\wireshark_ssl\private-key.pem" -o ssl.debug_file:"e:\temp\ssl-debug.log" -V -R http</p><p>It seems only work with key file in PEM format without passphrase, I can't use a p12 format cert file with private key even I provide the passphrase for the private key like in Wireshark.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Aug '11, 18:36</strong></p><img src="https://secure.gravatar.com/avatar/f3921a78dc931a180863fc5cd3b142ee?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Raymond%20Wang&#39;s gravatar image" /><p><span>Raymond Wang</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Raymond Wang has one accepted answer">100%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Feb '12, 05:06</strong> </span></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p><span>grahamb ♦</span><br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-5878" class="comments-container"><span id="5879"></span><div id="comment-5879" class="comment"><div id="post-5879-score" class="comment-score"></div><div class="comment-text"><p>Check the option string in ssl_keys file, I find all the backslash in the key file path are lost in my answer.</p></div><div id="comment-5879-info" class="comment-info"><span class="comment-age">(25 Aug '11, 18:41)</span> <span class="comment-user userinfo">Raymond Wang</span></div></div><span id="8924"></span><div id="comment-8924" class="comment"><div id="post-8924-score" class="comment-score"></div><div class="comment-text"><p>thanks, and sorry for the late response. Works in 1.6.2, but seems that it doesn't work anymore in 1.6.5 ... investigating further</p></div><div id="comment-8924-info" class="comment-info"><span class="comment-age">(09 Feb '12, 04:07)</span> <span class="comment-user userinfo">r0u1i</span></div></div><span id="8926"></span><div id="comment-8926" class="comment"><div id="post-8926-score" class="comment-score"></div><div class="comment-text"><p>To display the "\" character in your answer, you need to "escape" it with another backslash. You also need to prefix an underscore with a backslash. I've fixed the backslashes and underscores in your answer.</p></div><div id="comment-8926-info" class="comment-info"><span class="comment-age">(09 Feb '12, 05:02)</span> <span class="comment-user userinfo">grahamb ♦</span></div></div><span id="45651"></span><div id="comment-45651" class="comment"><div id="post-45651-score" class="comment-score"></div><div class="comment-text"><p>the private-key.pem is on web-server? i want use to call the remote server.... fiddler dont need any key file,but that only support windows.</p></div><div id="comment-45651-info" class="comment-info"><span class="comment-age">(07 Sep '15, 00:30)</span> <span class="comment-user userinfo">zhylninc</span></div></div></div><div id="comment-tools-5878" class="comment-tools"></div><div class="clear"></div><div id="comment-5878-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

