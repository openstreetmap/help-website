+++
type = "question"
title = "rpm Packaging error"
description = '''I have tried to do the packaging of wireshark-1.6.1  OS: Fedora 2.6.35.6-45.fc14.x86_64 # make rpm-package results in : configure: error: SSL crypto library was requested, but is not available error: Bad exit status from /var/tmp/rpm-tmp.k6KXRS (%prep) RPM build errors:  Bad exit status from /var/tm...'''
date = "2011-09-14T01:10:00Z"
lastmod = "2011-09-14T04:13:00Z"
weight = 6344
keywords = [ "packaging" ]
aliases = [ "/questions/6344" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [rpm Packaging error](/questions/6344/rpm-packaging-error)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6344-score" class="post-score" title="current number of votes">0</div><span id="post-6344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count">1</div></div></td><td><div id="item-right"><div class="question-body"><p>I have tried to do the packaging of wireshark-1.6.1</p><p>OS: Fedora 2.6.35.6-45.fc14.x86_64</p><p><code># make rpm-package</code> results in :</p><pre><code>configure: error: SSL crypto library was requested, but is not available
error: Bad exit status from /var/tmp/rpm-tmp.k6KXRS (%prep)
RPM build errors:
    Bad exit status from /var/tmp/rpm-tmp.k6KXRS (%prep)
make: *** [rpm-package] Error 1</code></pre></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-packaging" rel="tag" title="see questions tagged &#39;packaging&#39;">packaging</span></div><div id="question-controls" class="post-controls"><div class="community-wiki">This question is marked "community wiki".</div></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>14 Sep '11, 01:10</strong></p><img src="https://secure.gravatar.com/avatar/264adc05b644c1ab2d670b4773a12392?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="flashkicker&#39;s gravatar image" /><p><span>flashkicker</span><br />
<span class="score" title="109 reputation points">109</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="flashkicker has 5 accepted answers">41%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>14 Sep '11, 04:08</strong> </span></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span></p></div></div><div id="comments-container-6344" class="comments-container"></div><div id="comment-tools-6344" class="comment-tools"></div><div class="clear"></div><div id="comment-6344-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="6352"></span>

<div id="answer-container-6352" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-6352-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-6352-score" class="post-score" title="current number of votes">1</div><span id="post-6352-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="flashkicker has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>Either setup the SSL library development files or adjust the configure command line <code>packaging/rpm/SPECS/wireshark.spec.in</code> by removing <code>--with-ssl</code></p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>14 Sep '11, 04:13</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p><span>Jaap ♦</span><br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-6352" class="comments-container"></div><div id="comment-tools-6352" class="comment-tools"></div><div class="clear"></div><div id="comment-6352-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

