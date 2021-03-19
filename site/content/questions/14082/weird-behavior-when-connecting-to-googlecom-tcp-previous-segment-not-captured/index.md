+++
type = "question"
title = "Weird behavior when connecting to google.com (TCP previous segment not captured)"
description = '''I had Ubuntu 11.10 and in the last few weeks I experienced an obscure problem: after I had the computer running for a few days I could no longer connect to google.com or anything related to google. All sites worked with all browsers (Firefox, chrome, opera) except google. It remained in the connecti...'''
date = "2012-09-06T04:24:00Z"
lastmod = "2012-09-08T06:45:00Z"
weight = 14082
keywords = [ "prev_seg_lost", "google", "tcp" ]
aliases = [ "/questions/14082" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Weird behavior when connecting to google.com (TCP previous segment not captured)](/questions/14082/weird-behavior-when-connecting-to-googlecom-tcp-previous-segment-not-captured)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14082-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14082-score" class="post-score" title="current number of votes">0</div><span id="post-14082-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I had Ubuntu 11.10 and in the last few weeks I experienced an obscure problem: after I had the computer running for a few days I could no longer connect to <a href="http://google.com">google.com</a> or anything related to google. All sites worked with all browsers (Firefox, chrome, opera) except google. It remained in the connecting phase for a few minutes and either timed out or finally connected with this huge delay.</p><p>Even if I entered other sites such as this one, if it had anything to do with google such adsense or gstatic or whatever with g in it, that site took a long time to load waiting in connecting to <a href="http://gstatic.com">gstatic.com</a> . Anything google related took minutes to work, but everything else worked instantly!</p><p>I tried rebooting or using other machine(with windows on it) and this worked, so it's not network related. But after a few days it started not working again... So I upgraded to the Precise Pangolin hoping this behavior would go away. It didn't! After a few days I get the same behavior as in 11.10.</p><p>What am I supposed to do? Reboot every other day?</p><p>I didn't have this problem with neither 10.10 or 11.04.</p><p>I found the Realtek RTL8168/8111E issue with the r8169 driver but this is not exactly the same card so probably trying r8168 won't help. After trying the new driver I still get the same behavior. I will show you what wireshark says when receiving data from google:</p><pre><code>No.     Time           Source                Destination           Protocol Length Info
113 12.354065000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421958317 TSecr=42206636 WS=64
130 12.402673000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421958366 TSecr=42206636 WS=64
146 12.608145000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421958571 TSecr=42206636 WS=64
156 12.656652000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421958619 TSecr=42206636 WS=64
157 12.747373000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421958711 TSecr=42206636 WS=64
161 12.821862000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421958785 TSecr=42206636 WS=64
163 13.147872000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421959111 TSecr=42206636 WS=64
167 13.347348000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421959311 TSecr=42206636 WS=64
168 13.351575000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421959315 TSecr=42206636 WS=64
170 13.400050000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421959363 TSecr=42206636 WS=64
171 13.421910000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421959385 TSecr=42206636 WS=64
177 13.604892000   74.125.232.219        192.168.1.100         TCP      74     [TCP Previous segment not captured] http &gt; matahari [SYN, ACK] Seq=15574924 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421959568 TSecr=42206636 WS=64
179 13.653929000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421959617 TSecr=42206636 WS=64
180 13.747964000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421959711 TSecr=42206636 WS=64
183 14.021338000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=15574924 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421959985 TSecr=42206636 WS=64
184 14.547381000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421960511 TSecr=42206636 WS=64
185 14.621228000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=15574924 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421960585 TSecr=42206636 WS=64
186 14.621700000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421960585 TSecr=42206636 WS=64
187 14.947683000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421960911 TSecr=42206636 WS=64
191 15.355729000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421961319 TSecr=42206636 WS=64
193 15.404014000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421961367 TSecr=42206636 WS=64
200 15.609680000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=15574924 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421961573 TSecr=42206636 WS=64
203 15.658207000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421961621 TSecr=42206636 WS=64
207 15.822131000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=15574924 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421961786 TSecr=42206636 WS=64
216 16.947171000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421962911 TSecr=42206636 WS=64
218 17.022812000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421962986 TSecr=42206636 WS=64
222 17.347885000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421963311 TSecr=42206636 WS=64
269 18.222432000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=15574924 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421964186 TSecr=42206636 WS=64
287 19.363611000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421965327 TSecr=42206636 WS=64
289 19.412078000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421965375 TSecr=42206636 WS=64
295 19.621025000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=15574924 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421965584 TSecr=42206636 WS=64
297 19.670286000   74.125.232.219        192.168.1.100         TCP      74     [TCP Previous segment not captured] http &gt; 49002 [SYN, ACK] Seq=109588186 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421965633 TSecr=42206636 WS=64
311 21.748560000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421967712 TSecr=42206636 WS=64
312 21.824699000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421967788 TSecr=42206636 WS=64
320 23.025160000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=15574924 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421968989 TSecr=42206636 WS=64
327 27.379578000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421973343 TSecr=42206636 WS=64
330 27.428045000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=0 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421973391 TSecr=42206636 WS=64
336 27.638004000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=15574924 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421973602 TSecr=42206636 WS=64
338 27.686163000   74.125.232.219        192.168.1.100         TCP      74     [TCP Previous segment not captured] http &gt; 49002 [SYN, ACK] Seq=234839129 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421973649 TSecr=42206636 WS=64
346 28.151691000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=234839129 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421974115 TSecr=42206636 WS=64
348 28.752715000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=234839129 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421974715 TSecr=42206636 WS=64
349 29.951576000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=234839129 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421975915 TSecr=42206636 WS=64
360 32.351634000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=234839129 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421978315 TSecr=42206636 WS=64
364 37.153511000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=234839129 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421983117 TSecr=42206636 WS=64
385 43.427848000   74.125.232.219        192.168.1.100         TCP      74     [TCP Previous segment not captured] http &gt; 48993 [SYN, ACK] Seq=485534174 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421989392 TSecr=42206636 WS=64
387 43.460361000   74.125.232.219        192.168.1.100         TCP      74     [TCP Previous segment not captured] http &gt; 48998 [SYN, ACK] Seq=485282700 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421989423 TSecr=42206636 WS=64
393 43.685892000   74.125.232.219        192.168.1.100         TCP      74     [TCP Previous segment not captured] http &gt; matahari [SYN, ACK] Seq=485596662 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421989650 TSecr=42206636 WS=64
395 43.718463000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 49002 [SYN, ACK] Seq=234839129 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421989682 TSecr=42206636 WS=64
396 43.754973000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=485534174 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421989719 TSecr=42206636 WS=64
398 43.834404000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=485282700 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421989798 TSecr=42206636 WS=64
400 44.033826000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=485596662 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421989998 TSecr=42206636 WS=64
401 44.354947000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=485534174 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421990319 TSecr=42206636 WS=64
402 44.435384000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=485282700 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421990398 TSecr=42206636 WS=64
403 44.633806000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=485596662 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421990598 TSecr=42206636 WS=64
404 45.554892000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=485534174 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421991519 TSecr=42206636 WS=64
405 45.634302000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=485282700 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421991598 TSecr=42206636 WS=64
406 45.833829000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=485596662 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421991798 TSecr=42206636 WS=64
411 47.956110000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48993 [SYN, ACK] Seq=485534174 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421993920 TSecr=42206636 WS=64
412 48.034301000   74.125.232.219        192.168.1.100         TCP      74     http &gt; 48998 [SYN, ACK] Seq=485282700 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421993998 TSecr=42206636 WS=64
414 48.234786000   74.125.232.219        192.168.1.100         TCP      74     http &gt; matahari [SYN, ACK] Seq=485596662 Ack=1 Win=14180 Len=0 MSS=1430 SACK_PERM=1 TSval=1421994198 TSecr=42206636 WS=64</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-prev_seg_lost" rel="tag" title="see questions tagged &#39;prev_seg_lost&#39;">prev_seg_lost</span> <span class="post-tag tag-link-google" rel="tag" title="see questions tagged &#39;google&#39;">google</span> <span class="post-tag tag-link-tcp" rel="tag" title="see questions tagged &#39;tcp&#39;">tcp</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>06 Sep '12, 04:24</strong></p><img src="https://secure.gravatar.com/avatar/dcc78b8aae162ba01b8b7cd1d5008293?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sebastian&#39;s gravatar image" /><p><span>Sebastian</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Sebastian has no accepted answers">0%</span></p></div></div><div id="comments-container-14082" class="comments-container"><span id="14119"></span><div id="comment-14119" class="comment"><div id="post-14119-score" class="comment-score"></div><div class="comment-text"><p>can you please post the whole conversation at <a href="http://cloudshark.org">cloudshark.org</a>? With only the SYN,ACK from google, it's hard to do any troubleshooting ;-)</p></div><div id="comment-14119-info" class="comment-info"><span class="comment-age">(07 Sep '12, 05:22)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-14082" class="comment-tools"></div><div class="clear"></div><div id="comment-14082-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="14098"></span>

<div id="answer-container-14098" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14098-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14098-score" class="post-score" title="current number of votes">0</div><span id="post-14098-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>First get a baseline of communications that work (like after a reboot). Then compare that to communications with other hosts, what is the difference? What TCP congestion avoidance algorithm or other extension can you find in that traffic? What networking equipment do you have between your computer and the internet? Can it handle these TCP connections properly?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>06 Sep '12, 14:35</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-14098" class="comments-container"><span id="14138"></span><div id="comment-14138" class="comment"><div id="post-14138-score" class="comment-score"></div><div class="comment-text"><p>I have tested 2 routers with the same behaviour (now I am on a TP_LINK Model No. TL-R402M). How do I find what congestion avoidance algorithm the network is using? I have two theories: since I tried kernel versions from the time this problem wasn't manifesting and I still get the behaviour I'm thinking it's either something newer in Ubuntu that doesn't have anything to do with the kernel that is causing the behaviour or something at my ISP changed. But if something at my ISP changed shouldn't I get the same behaviour on Windows machines? Is the tcp stack really that different?</p></div><div id="comment-14138-info" class="comment-info"><span class="comment-age">(08 Sep '12, 06:45)</span> <span class="comment-user userinfo">Sebastian</span></div></div></div><div id="comment-tools-14098" class="comment-tools"></div><div class="clear"></div><div id="comment-14098-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="14118"></span>

<div id="answer-container-14118" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-14118-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-14118-score" class="post-score" title="current number of votes">0</div><span id="post-14118-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I have noticed that with Google mail at least it likes the time and date reasonably close to reality. No idea how it checks or whether you reached the point at which it checks though. The error when I was way off was Too Many Redirects which at least is consistent with things slowing down. Just a thought.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Sep '12, 04:34</strong></p><img src="https://secure.gravatar.com/avatar/4b31b42b2960269c605715bae6547459?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MartinM&#39;s gravatar image" /><p><span>MartinM</span><br />
<span class="score" title="167 reputation points">167</span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MartinM has 3 accepted answers">33%</span></p></div></div><div id="comments-container-14118" class="comments-container"></div><div id="comment-tools-14118" class="comment-tools"></div><div class="clear"></div><div id="comment-14118-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

