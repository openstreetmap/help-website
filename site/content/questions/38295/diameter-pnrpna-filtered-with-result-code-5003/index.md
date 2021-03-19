+++
type = "question"
title = "Diameter PNR/PNA filtered with result code 5003"
description = '''Hello, I have a difficulty to use MATE plugin to filter diameter.cmd.code==309 &amp;amp;&amp;amp; diameter.Result-Code==5003. I would like to get both request (PNR) and the Answer (PNA). This is the draft that I can think of, but no sure how to modify it to meet my requirement. // Create a &quot;diam_pdu&quot; that c...'''
date = "2014-12-02T23:05:00Z"
lastmod = "2015-03-23T22:18:00Z"
weight = 38295
keywords = [ "diameter", "mate" ]
aliases = [ "/questions/38295" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Diameter PNR/PNA filtered with result code 5003](/questions/38295/diameter-pnrpna-filtered-with-result-code-5003)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38295-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38295-score" class="post-score" title="current number of votes">0</div><span id="post-38295-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello,</p><p>I have a difficulty to use MATE plugin to filter diameter.cmd.code==309 &amp;&amp; diameter.Result-Code==5003. I would like to get both request (PNR) and the Answer (PNA).</p><p>This is the draft that I can think of, but no sure how to modify it to meet my requirement.</p><pre><code>// Create a &quot;diam_pdu&quot; that contains various pieces of the processed Diameter
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

Done;</code></pre><p>Please kindly help me to resolve it, thanks!</p><p>Alex</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-diameter" rel="tag" title="see questions tagged &#39;diameter&#39;">diameter</span> <span class="post-tag tag-link-mate" rel="tag" title="see questions tagged &#39;mate&#39;">mate</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '14, 23:05</strong></p><img src="https://secure.gravatar.com/avatar/c6d2de8ff58f1dc3175ac84d437c5931?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alex%20Lu&#39;s gravatar image" /><p><span>Alex Lu</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alex Lu has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>03 Dec '14, 06:41</strong> </span></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-38295" class="comments-container"></div><div id="comment-tools-38295" class="comment-tools"></div><div class="clear"></div><div id="comment-38295-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="38304"></span>

<div id="answer-container-38304" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-38304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-38304-score" class="post-score" title="current number of votes">0</div><span id="post-38304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JeffMorriss has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>To do that you'll need to store the Result-Code in the GOP. So this configuration file:</p><pre><code>// Create a &quot;diam_pdu&quot; that contains various pieces of the processed Diameter
// message.
Pdu diam_pdu Proto diameter Transport ip {
        Extract command_code From diameter.cmd.code;
        Extract app_id From diameter.applicationId;
        Extract session_id From diameter.Session-Id;
        Extract e2eid From diameter.endtoendid;
        Extract resultcode From diameter.Result-Code;
};

// Then create a GOP (Group Of Pdus) where the each GOP contains all the PDUs
// (msgs) that whose command_code, app_id, session_id, and e2eid match.
Gop diam_transaction On diam_pdu Match (command_code, app_id, session_id, e2eid) {
        Start();
        Stop(never);

        // Store the result code in the GOP
        Extra(resultcode);
};

Done;</code></pre><p>with a display filter of:</p><pre><code>(mate.diam_transaction.command_code == &quot;309&quot;) &amp;&amp; (mate.diam_transaction.resultcode == &quot;5003&quot;)</code></pre><p>will show you both the Request(s) and their corresponding Answer(s).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Dec '14, 06:54</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p><span>JeffMorriss ♦</span><br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>09 Jan '15, 08:04</strong> </span></p></div></div><div id="comments-container-38304" class="comments-container"><span id="38726"></span><div id="comment-38726" class="comment"><div id="post-38726-score" class="comment-score"></div><div class="comment-text"><p>Thank you very much, Jeff!</p><p>Somehow it is still not working as expected.</p><p>Could it be caused by</p><pre><code>    Start();
    Stop(never);</code></pre><p>Thanks again.</p></div><div id="comment-38726-info" class="comment-info"><span class="comment-age">(26 Dec '14, 20:41)</span> <span class="comment-user userinfo">Alex Lu</span></div></div><span id="39003"></span><div id="comment-39003" class="comment"><div id="post-39003-score" class="comment-score">1</div><div class="comment-text"><p>(Sorry, I was offline over the holidays.)</p><p>(BTW I converted your Answer to a Comment.)</p><p>Are you putting quotes around the command code and resultcode (as shown in the example above)? It wasn't working for me, either, when I typed in the filter by hand but when I used "prepare as filter" it worked well--and I noticed that "prepare as filter" was putting the quotes in there.</p><p>(It is annoying that the quotes must be there; I guess MATE's fields are all strings? That's worth of investigation--if I have time &lt;sigh&gt;.)</p></div><div id="comment-39003-info" class="comment-info"><span class="comment-age">(09 Jan '15, 08:03)</span> <span class="comment-user userinfo">JeffMorriss ♦</span></div></div><span id="40791"></span><div id="comment-40791" class="comment"><div id="post-40791-score" class="comment-score"></div><div class="comment-text"><p>Works flawless! Thank you Jeff!</p></div><div id="comment-40791-info" class="comment-info"><span class="comment-age">(23 Mar '15, 22:18)</span> <span class="comment-user userinfo">Alex Lu</span></div></div></div><div id="comment-tools-38304" class="comment-tools"></div><div class="clear"></div><div id="comment-38304-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

