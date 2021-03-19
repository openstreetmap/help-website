+++
type = "question"
title = "Strange SSL capture: &quot;Ignored Unknown Record&quot; instead of ServerHello"
description = '''Hi - I&#x27;ve been trying to decrypt an SSL stream from a single client to one of our servers. Since I was unable to decode it, I thought it may have been as a result of DH key negotiation, but the trace I took just seemed too odd. You can see that packet 11 is summarized by Wireshark (1.4.6) as &#x27;Ignore...'''
date = "2011-06-01T15:03:00Z"
lastmod = "2011-06-02T13:03:00Z"
weight = 4320
keywords = [ "ssl", "dhe", "decrypt" ]
aliases = [ "/questions/4320" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Strange SSL capture: "Ignored Unknown Record" instead of ServerHello](/questions/4320/strange-ssl-capture-ignored-unknown-record-instead-of-serverhello)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4320-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4320-score" class="post-score" title="current number of votes">0</div><span id="post-4320-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi - I've been trying to decrypt an SSL stream from a single client to one of our servers. Since I was unable to decode it, I thought it may have been as a result of DH key negotiation, but the trace I took just seemed too odd.</p><p>You can see that packet 11 is summarized by Wireshark (1.4.6) as 'Ignored Unknown Record' at the point where I would expect 'Server Hello'</p><p>The capture was taken on the Linux box which acts as a load balancer in our network, so it's right bang in the middle of the data path between client and server. Commandline:</p><pre><code>tcpdump -i bond0.397 -n host 46.51.172.223 and port 443 -s 1500 -w out.cap</code></pre><p>Here is the capture: <a href="http://194.24.251.10/oddssl.cap">http://194.24.251.10/oddssl.cap</a></p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-ssl" rel="tag" title="see questions tagged &#39;ssl&#39;">ssl</span> <span class="post-tag tag-link-dhe" rel="tag" title="see questions tagged &#39;dhe&#39;">dhe</span> <span class="post-tag tag-link-decrypt" rel="tag" title="see questions tagged &#39;decrypt&#39;">decrypt</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Jun '11, 15:03</strong></p><img src="https://secure.gravatar.com/avatar/73d9810c3e5f657391900c01e288d911?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gdhgdh&#39;s gravatar image" /><p><span>gdhgdh</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gdhgdh has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>01 Jun '11, 15:09</strong> </span></p></div></div><div id="comments-container-4320" class="comments-container"></div><div id="comment-tools-4320" class="comment-tools"></div><div class="clear"></div><div id="comment-4320-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="4325"></span>

<div id="answer-container-4325" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-4325-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-4325-score" class="post-score" title="current number of votes">2</div><span id="post-4325-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="gdhgdh has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You used a snaplength of 1500, while packets can be 1514 bytes (or 1518 when the FCS is not stripped by the NIC). As you can see in the frame-header, 14 bytes were lost, so Wireshark is not able to do reassembly.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jun '11, 22:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-4325" class="comments-container"><span id="4342"></span><div id="comment-4342" class="comment"><div id="post-4342-score" class="comment-score"></div><div class="comment-text"><p>&lt;blush&gt; I feel very silly. Thank you for pointing the snaplen out.</p><p>FWIW my theory about DH key exchange was right, and now I have the proof. Trebles all round =)</p></div><div id="comment-4342-info" class="comment-info"><span class="comment-age">(02 Jun '11, 10:58)</span> <span class="comment-user userinfo">gdhgdh</span></div></div><span id="4347"></span><div id="comment-4347" class="comment"><div id="post-4347-score" class="comment-score"></div><div class="comment-text"><p>No Worries, we all have our less ingenious moments ;-)</p><p>About the DH key exchange, you are indeed not able to decrypt them with the server key. However, Chrome and Firefox can now be built with SSL debugging on, so that it saves the pre-master secrets to file and you can import them in Wireshark.</p><p>Another possibility is to (temporarily) disable all DH cipers on the server side so that a non-DH gets chosen so you can do your troubleshooting on the decrypted traffic.</p></div><div id="comment-4347-info" class="comment-info"><span class="comment-age">(02 Jun '11, 13:03)</span> <span class="comment-user userinfo">SYN-bit ♦♦</span></div></div></div><div id="comment-tools-4325" class="comment-tools"></div><div class="clear"></div><div id="comment-4325-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

