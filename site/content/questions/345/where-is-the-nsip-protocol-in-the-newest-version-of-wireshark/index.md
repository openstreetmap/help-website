+++
type = "question"
title = "Where is the NSIP protocol in the newest version of Wireshark?"
description = '''where is nsip protocol in the newest version of wireshark, i can&#x27;t find it when using &quot;decode as&quot; option'''
date = "2010-09-28T01:17:00Z"
lastmod = "2010-09-28T17:40:00Z"
weight = 345
keywords = [ "nsip", "gprs-ns", "wireshark" ]
aliases = [ "/questions/345" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Where is the NSIP protocol in the newest version of Wireshark?](/questions/345/where-is-the-nsip-protocol-in-the-newest-version-of-wireshark)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-345-score" class="post-score" title="current number of votes">0</div><span id="post-345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>where is nsip protocol in the newest version of wireshark, i can't find it when using "decode as" option</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-nsip" rel="tag" title="see questions tagged &#39;nsip&#39;">nsip</span> <span class="post-tag tag-link-gprs-ns" rel="tag" title="see questions tagged &#39;gprs-ns&#39;">gprs-ns</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Sep '10, 01:17</strong></p><img src="https://secure.gravatar.com/avatar/14e9627735393ca051150547b367754e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wxg&#39;s gravatar image" /><p><span>wxg</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wxg has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>28 Sep '10, 09:01</strong> </span></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span></p></div></div><div id="comments-container-345" class="comments-container"></div><div id="comment-tools-345" class="comment-tools"></div><div class="clear"></div><div id="comment-345-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="347"></span>

<div id="answer-container-347" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-347-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-347-score" class="post-score" title="current number of votes">1</div><span id="post-347-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>It looks like the NSIP dissector was renamed to GPRS-NS back in March. Here is the commit message from SVN revision 32295:</p><pre><code>From Mike Morrin:
There were 2 dissectors for GPRS-NS (GSM 48.016) protocol, packet-gprs-ns.c and
packet-gprs-ns.c.  packet-nsip.c seemed to be the more complete, and has a
cleaner output.

I have polished up nsip.c and changed it so that it identifies itself as the
dissector for gprs-ns.

packet-gprs-ns.c can be deleted.</code></pre><p>Does "Decode As" GPRS-NS work?</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Sep '10, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/6db117a984c6529df88330dc49fb1ee4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gerald%20Combs&#39;s gravatar image" /><p><span>Gerald Combs ♦♦</span><br />
<span class="score" title="3332 reputation points"><span>3.3k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="58 badges"><span class="bronze">●</span><span class="badgecount">58</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gerald Combs has 32 accepted answers">24%</span></p></div></div><div id="comments-container-347" class="comments-container"><span id="351"></span><div id="comment-351" class="comment"><div id="post-351-score" class="comment-score"></div><div class="comment-text"><p>yes it works! thank u</p></div><div id="comment-351-info" class="comment-info"><span class="comment-age">(28 Sep '10, 17:40)</span> <span class="comment-user userinfo">wxg</span></div></div></div><div id="comment-tools-347" class="comment-tools"></div><div class="clear"></div><div id="comment-347-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

