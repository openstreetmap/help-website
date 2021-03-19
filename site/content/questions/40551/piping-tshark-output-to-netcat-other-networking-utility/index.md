+++
type = "question"
title = "piping tshark output to netcat / other networking utility"
description = '''Hi folks,  I need to pipe the results of this:  sudo tshark -I -l -q -i en1 -T fields -e wlan.sa_resolved -e wlan_mgt.ssid -e radiotap.dbm_antsignal &quot;type mgt subtype probe-req&quot; | sed -e &#x27;s:^:/:&#x27;  which look like this:  /00:15:99:b3:ec:e1 ZiggoDBD4C -76 /00:15:99:b3:ec:e1 ZiggoDBD4C -76 /00:15:99:b3...'''
date = "2015-03-14T03:22:00Z"
lastmod = "2015-03-14T05:18:00Z"
weight = 40551
keywords = [ "netcat", "udp", "networking", "tshark", "bash" ]
aliases = [ "/questions/40551" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [piping tshark output to netcat / other networking utility](/questions/40551/piping-tshark-output-to-netcat-other-networking-utility)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40551-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40551-score" class="post-score" title="current number of votes">0</div><span id="post-40551-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks,</p><p>I need to pipe the results of this:</p><pre><code>  sudo tshark -I -l -q -i en1 -T fields -e wlan.sa_resolved -e wlan_mgt.ssid -e radiotap.dbm_antsignal &quot;type mgt subtype probe-req&quot; | sed -e &#39;s:^:/:&#39;</code></pre><p>which look like this:</p><pre><code>/00:15:99:b3:ec:e1  ZiggoDBD4C  -76
/00:15:99:b3:ec:e1  ZiggoDBD4C  -76
/00:15:99:b3:ec:e1  ZiggoDBD4C  -75</code></pre><p>into a networking utility, such as netcat or sendOSC (I'm receiving the results in Puredata). When I try to run somthing like</p><pre><code>sudo tshark -I -l -q -i en1 -T fields -e wlan.sa_resolved -e wlan_mgt.ssid -e radiotap.dbm_antsignal &quot;type mgt subtype probe-req&quot; | sed -e &#39;s:^:/:&#39; | nc localhost 9997</code></pre><p>I get no output from tshark shown, though when I cancel the tshark scan I had definitely captured packets. Anyone know why this is?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-netcat" rel="tag" title="see questions tagged &#39;netcat&#39;">netcat</span> <span class="post-tag tag-link-udp" rel="tag" title="see questions tagged &#39;udp&#39;">udp</span> <span class="post-tag tag-link-networking" rel="tag" title="see questions tagged &#39;networking&#39;">networking</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-bash" rel="tag" title="see questions tagged &#39;bash&#39;">bash</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Mar '15, 03:22</strong></p><img src="https://secure.gravatar.com/avatar/6ad9c485468672305ea947f0acdebd32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="youcloudsofddom&#39;s gravatar image" /><p><span>youcloudsofddom</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="youcloudsofddom has no accepted answers">0%</span></p></div></div><div id="comments-container-40551" class="comments-container"></div><div id="comment-tools-40551" class="comment-tools"></div><div class="clear"></div><div id="comment-40551-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40553"></span>

<div id="answer-container-40553" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40553-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40553-score" class="post-score" title="current number of votes">2</div><span id="post-40553-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="youcloudsofddom has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Just like you need to make tshark line-buffered, you also need to make sed line-buffered for data to pass through the pipes real-time. Add <code>-l</code> to the sed command :-)</p><p>See <a href="http://www.pixelbeat.org/programming/stdio_buffering/">this great article</a> on the use of buffers while piping output. Just found it by googling, so thank you for your question ;-)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Mar '15, 03:48</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40553" class="comments-container"><span id="40560"></span><div id="comment-40560" class="comment"><div id="post-40560-score" class="comment-score"></div><div class="comment-text"><p>Ah, thank you again SYN-bit! That article was very useful - turns out what was needed was stdbuf -oL in with the sed command. Didn't even know that pipe had those issues. Thanks for all your help!</p></div><div id="comment-40560-info" class="comment-info"><span class="comment-age">(14 Mar '15, 05:18)</span> <span class="comment-user userinfo">youcloudsofddom</span></div></div></div><div id="comment-tools-40553" class="comment-tools"></div><div class="clear"></div><div id="comment-40553-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

