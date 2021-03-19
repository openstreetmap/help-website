+++
type = "question"
title = "Wireshark MATE - AVPL Merge"
description = '''Hi, I’m trying to analyze (combine) RADIUS traffic (and eventually other traffic) using Wireshark MATE plugin. What I would like to do is to Merge MATE Pdu attributes in case radius.id is the same for two different RADIUS packages. Main reason for this Merge is to have radius.State copied in MATE Pd...'''
date = "2014-04-16T05:14:00Z"
lastmod = "2014-04-17T06:58:00Z"
weight = 31879
keywords = [ "mate" ]
aliases = [ "/questions/31879" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Wireshark MATE - AVPL Merge](/questions/31879/wireshark-mate-avpl-merge)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31879-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31879-score" class="post-score" title="current number of votes">0</div><span id="post-31879-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi,</p><p>I’m trying to analyze (combine) RADIUS traffic (and eventually other traffic) using Wireshark MATE plugin.</p><p>What I would like to do is to Merge MATE Pdu attributes in case radius.id is the same for two different RADIUS packages. Main reason for this Merge is to have radius.State copied in MATE Pdu for first Access-Request and Access-Accept (Access-Reject) packages (radius.State is not in first and last message of the RADIUS session). After that I would be able to use MATE Pdu radius.State in MATE Gop definition and I would have all RADIUS messages related to one session inside one MATE Gop.</p><p><strong>So in short I’m trying to check if MATE Pdu Merge function is available or not and syntax if it is available.</strong> Or if similar function can be achieved using available functions e.g. MATE Transform function. AVPL Merge is mentioned in MATE wiki on <a href="http://wiki.wireshark.org/Mate/Reference#Merge">http://wiki.wireshark.org/Mate/Reference#Merge</a></p><p>I was also checking MATE source code on <a href="https://github.com/avsej/wireshark/blob/master/plugins/mate/">https://github.com/avsej/wireshark/blob/master/plugins/mate/</a> but I’m not expert in C.</p><p>From RFC 2865: 5.24. State This Attribute is available to be sent by the server to the client in an Access-Challenge and MUST be sent unmodified from the client to the server in the new Access-Request reply to that challenge, if any.</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Apr '14, 05:14</strong></p><img src="https://secure.gravatar.com/avatar/abfb8f438bcfaa68659ed3400c4c6191?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Danijel&#39;s gravatar image" /><p><span>Danijel</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Danijel has no accepted answers">0%</span></p></div></div><div id="comments-container-31879" class="comments-container"></div><div id="comment-tools-31879" class="comment-tools"></div><div class="clear"></div><div id="comment-31879-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="31898"></span>

<div id="answer-container-31898" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-31898-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-31898-score" class="post-score" title="current number of votes">2</div><span id="post-31898-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Danijel has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I'm pretty sure (though I'm far from an expert in MATE) that you can't merge Pdus. You can merge AVPLs (as the wiki says) but only in Gops or Gogs. So what you should probably do is create a Gop which has all the values you want and then, if needed, create a Gog for the session.</p><p>BTW the right place to look at Wireshark's source code is on <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree">code.wireshark.org</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Apr '14, 10:03</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-31898" class="comments-container"><span id="31911"></span><div id="comment-31911" class="comment"><div id="post-31911-score" class="comment-score"></div><div class="comment-text"><p>Hi,<br />
Thanks for pointing out that correct source code address for MATE is <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree;f=plugins/mate">https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree;f=plugins/mate</a><br />
By looking at this MATE source code (mate_grammar.lemon and mate_parser.l) I'm still not able to find "Merge" keyword.</p><p>Do you know what would be syntax for merging AVPLs in Gops or Gogs?<br />
</p><p>I think that Merge function for Pdus would be great (if it doesn't already exist :-)). It would increase MATE usability in so many ways.</p></div><div id="comment-31911-info" class="comment-info"><span class="comment-age">(17 Apr '14, 01:01)</span> <span class="comment-user userinfo">Danijel</span></div></div><span id="31928"></span><div id="comment-31928" class="comment"><div id="post-31928-score" class="comment-score"></div><div class="comment-text"><p>Ah, OK, getting parameters from a Pdu to a Gop isn't done with a "merge" keyword, it's done with the "Extra" key word. Here's an example (look for the "Extra" line with comment):</p><pre><code>// A Wireshark MATE configuration file to identify Diameter transactions.

// Create a &quot;diam_pdu&quot; that contains various pieces of the processed Diameter
// message.
Pdu diam_pdu Proto diameter Transport ip {
        Extract command_code From diameter.cmd.code;
        Extract app_id From diameter.applicationId;
        Extract session_id From diameter.Session-Id;
        Extract imsi From diameter.User-Name;
        Extract e2eid From diameter.endtoendid;
};

// Then create a GOP (Group Of Pdus) where the each GOP contains all the PDUs
// (msgs) that whose command_code, app_id, session_id, and e2eid match.
Gop diam_transaction On diam_pdu Match (command_code, app_id, session_id, e2eid) {
        Start();
        Stop(never);

        // Store the IMSI in the GOP
        Extra(imsi);
};

Done;</code></pre></div><div id="comment-31928-info" class="comment-info"><span class="comment-age">(17 Apr '14, 06:42)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="31929"></span><div id="comment-31929" class="comment"><div id="post-31929-score" class="comment-score"></div><div class="comment-text"><p>Thanks.<br />
This explains a lot.<br />
I will check if I can contribute with MATE wiki update.<br />
BR</p></div><div id="comment-31929-info" class="comment-info"><span class="comment-age">(17 Apr '14, 06:58)</span> <span class="comment-user userinfo">Danijel</span></div></div></div><div id="comment-tools-31898" class="comment-tools"></div><div class="clear"></div><div id="comment-31898-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

