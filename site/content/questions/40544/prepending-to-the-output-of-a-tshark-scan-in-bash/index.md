+++
type = "question"
title = "Prepending &#x27;/&#x27; to the output of a tshark scan in BASH"
description = '''Hi Folks, I&#x27;m running this tshark scan + filter: sudo tshark -I -i en1 -T fields -e wlan.sa_resolved -e wlan_mgt.ssid -e radiotap.dbm_antsignal type mgt subtype probe-req and need to prepend each line with a &#x27;/&#x27;, to get an output like this: /Apple_9d:ex:xx eduroam -90  I&#x27;ve tried sed &#x27;s:^:/:&#x27;and als...'''
date = "2015-03-13T16:00:00Z"
lastmod = "2015-03-13T16:39:00Z"
weight = 40544
keywords = [ "sed", "awk", "tshark", "bash", "prepend" ]
aliases = [ "/questions/40544" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Prepending '/' to the output of a tshark scan in BASH](/questions/40544/prepending-to-the-output-of-a-tshark-scan-in-bash)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40544-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40544-score" class="post-score" title="current number of votes">0</div><span id="post-40544-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi Folks,</p><p>I'm running this tshark scan + filter: <code>sudo tshark -I -i en1 -T fields -e wlan.sa_resolved -e wlan_mgt.ssid -e radiotap.dbm_antsignal type mgt subtype probe-req</code></p><p>and need to prepend each line with a '/', to get an output like this:</p><pre><code>/Apple_9d:ex:xx eduroam -90</code></pre><p>I've tried <code>sed 's:^:/:'</code>and also <code>| awk '{print " / " $0}'</code>but both of those stop the output of the scan from displaying (the packet counter appears instead). The only way I've got it to almost work is with <code>sudo tshark -I -i en1 -T fields -e wlan.sa_resolved -e wlan_mgt.ssid -e radiotap.dbm_antsignal type mgt subtype probe-req &gt; &gt;(sed 's:^:/:')</code>, but then you only see the output when you stop the command. Very furstrating.</p><p>I believe it's something to do with the probe request<code>type</code> filter, as when I remove that both sed &amp; awk work, but then I'm getting lots of frames etc that I don't need. Any thoughts would be greatly appreciated!</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-sed" rel="tag" title="see questions tagged &#39;sed&#39;">sed</span> <span class="post-tag tag-link-awk" rel="tag" title="see questions tagged &#39;awk&#39;">awk</span> <span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span> <span class="post-tag tag-link-bash" rel="tag" title="see questions tagged &#39;bash&#39;">bash</span> <span class="post-tag tag-link-prepend" rel="tag" title="see questions tagged &#39;prepend&#39;">prepend</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>13 Mar '15, 16:00</strong></p><img src="https://secure.gravatar.com/avatar/6ad9c485468672305ea947f0acdebd32?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="youcloudsofddom&#39;s gravatar image" /><p><span>youcloudsofddom</span><br />
<span class="score" title="16 reputation points">16</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="youcloudsofddom has no accepted answers">0%</span></p></div></div><div id="comments-container-40544" class="comments-container"></div><div id="comment-tools-40544" class="comment-tools"></div><div class="clear"></div><div id="comment-40544-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="40545"></span>

<div id="answer-container-40545" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-40545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-40545-score" class="post-score" title="current number of votes">1</div><span id="post-40545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="youcloudsofddom has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>How about using <code>-l</code> to make the output line buffered and <code>-q</code> to make it quiet about the packet count:</p><pre><code>$ sudo tshark -I -l -q -i en1 -T fields -e wlan.sa_resolved -e wlan_mgt.ssid -e radiotap.dbm_antsignal &quot;type mgt subtype probe-req&quot; | sed -e &#39;s:^:/:&#39;
Capturing on &#39;AirPort&#39;
/00:15:99:b3:ec:e1  ZiggoDBD4C  -76
/00:15:99:b3:ec:e1  ZiggoDBD4C  -76
/00:15:99:b3:ec:e1  ZiggoDBD4C  -75
/00:15:99:b3:ec:e1  ZiggoDBD4C  -75
/14:b4:84:7f:38:fe      -79
/14:b4:84:7f:38:fe      -80
/14:b4:84:7f:38:fe      -81
/14:b4:84:7f:38:fe      -79
/14:b4:84:7f:38:fe      -81
/00:15:99:b3:ec:e1  ZiggoDBD4C  -75
/00:15:99:b3:ec:e1  ZiggoDBD4C  -76
/00:15:99:b3:ec:e1  ZiggoDBD4C  -75
/00:15:99:b3:ec:e1  ZiggoDBD4C  -75
/00:15:99:b3:ec:e1  ZiggoDBD4C  -76
/00:15:99:b3:ec:e1  ZiggoDBD4C  -75
^C15 packets captured</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>13 Mar '15, 16:21</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-40545" class="comments-container"><span id="40546"></span><div id="comment-40546" class="comment"><div id="post-40546-score" class="comment-score"></div><div class="comment-text"><p>That works perfectly, thank you!</p></div><div id="comment-40546-info" class="comment-info"><span class="comment-age">(13 Mar '15, 16:39)</span> <span class="comment-user userinfo">youcloudsofddom</span></div></div></div><div id="comment-tools-40545" class="comment-tools"></div><div class="clear"></div><div id="comment-40545-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

