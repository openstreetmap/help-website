+++
type = "question"
title = "Latest Wireshark 1.4.4 not shown &quot;Granted QoS&quot; field existed in RNC A11 packet"
description = '''Hi, I opened the file A11-RNC-PCF.pcap with Wireshark 0.99.5 and found the ‘Granted QoS’ field in the A11 Reg Request packet from RNC to PDSN. But unfortunately if I used Wireshark version 1.4.4 there are not such field existed!? It quite mislead our customers who used latest version of Wireshark. I...'''
date = "2011-04-12T10:49:00Z"
lastmod = "2011-04-14T08:11:00Z"
weight = 3465
keywords = [ "qos" ]
aliases = [ "/questions/3465" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Latest Wireshark 1.4.4 not shown "Granted QoS" field existed in RNC A11 packet](/questions/3465/latest-wireshark-144-not-shown-granted-qos-field-existed-in-rnc-a11-packet)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3465-score" class="post-score" title="current number of votes">0</div><span id="post-3465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I opened the file A11-RNC-PCF.pcap with Wireshark 0.99.5 and found the ‘Granted QoS’ field in the A11 Reg Request packet from RNC to PDSN. But unfortunately if I used Wireshark version 1.4.4 there are not such field existed!? It quite mislead our customers who used latest version of Wireshark. Is this some bug? Below is parsed part of Wireshark output:</p><pre><code>Extension: Normal Vendor/Organization Specific Extension
            Extension Type: Normal Vendor/Organization Specific Extension (134)
            Extension Length: 22
            Vendor ID: 3rd Generation Partnership Project 2 (3GPP2) (0x0000159f)
            Application Type: Forward QoS Information (0xd01)
            SRID: 2
            Flags: 0x80
            Forward Flow Count: 1
            Forward Flow Entry (Flow Id: 0)
                Entry Length: 10
                Forward Flow Id: 0
                DSCP and Flow State: 0x5c
                    .... ...0 = Flow State: Inactive
                Requested QoS Length: 5
                Requested QoS: 7260402000
                Granted QoS Length: 1
                Granted QoS: 02</code></pre><p>Thanks for the advise.</p><p>Mikhail Boev Ericsson Canada</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-qos" rel="tag" title="see questions tagged &#39;qos&#39;">qos</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Apr '11, 10:49</strong></p><img src="https://secure.gravatar.com/avatar/e7fb507ca72752ebcbc12bf5e3cd5265?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mikhailboev&#39;s gravatar image" /><p><span>mikhailboev</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mikhailboev has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>12 Apr '11, 12:11</strong> </span></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p><span>SYN-bit ♦♦</span><br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span></p></div></div><div id="comments-container-3465" class="comments-container"></div><div id="comment-tools-3465" class="comment-tools"></div><div class="clear"></div><div id="comment-3465-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="3471"></span>

<div id="answer-container-3471" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-3471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-3471-score" class="post-score" title="current number of votes">0</div><span id="post-3471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>This may very well be a bug. You might want to <a href="https://bugs.wireshark.org/bugzilla/">open a bug report</a> and if possible, post the <code>A11-RNC-PCF.pcap</code> capture file to it, or at least one relevant packet from it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Apr '11, 13:20</strong></p><img src="https://secure.gravatar.com/avatar/55158e2322c4e365a5e0a4a0ac3fbcef?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="cmaynard&#39;s gravatar image" /><p><span>cmaynard ♦♦</span><br />
<span class="score" title="9361 reputation points"><span>9.4k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="38 badges"><span class="silver">●</span><span class="badgecount">38</span></span><span title="142 badges"><span class="bronze">●</span><span class="badgecount">142</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="cmaynard has 108 accepted answers">20%</span></p></div></div><div id="comments-container-3471" class="comments-container"><span id="3500"></span><div id="comment-3500" class="comment"><div id="post-3500-score" class="comment-score">1</div><div class="comment-text"><p>Just a followup for anyone who might be concerned with this: The bug was filed as <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=5822">bug 5822</a> and a fix was made in r36642. The fix will be back-ported to 1.4.x. For more details, refer to the bug report.</p></div><div id="comment-3500-info" class="comment-info"><span class="comment-age">(14 Apr '11, 08:11)</span> <span class="comment-user userinfo">cmaynard ♦♦</span></div></div></div><div id="comment-tools-3471" class="comment-tools"></div><div class="clear"></div><div id="comment-3471-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

