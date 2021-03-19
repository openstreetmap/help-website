+++
type = "question"
title = "pattern filter"
description = '''how to filter either strings at once ? I wrote something like this:  -Y &quot;tcp contains &quot;hi&quot;&quot; || tcp contains &quot;bye&quot;&quot; but it doesnt works, anyone please help? Thanks'''
date = "2017-06-20T21:36:00Z"
lastmod = "2017-06-20T23:21:00Z"
weight = 62197
keywords = [ "tshark" ]
aliases = [ "/questions/62197" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [pattern filter](/questions/62197/pattern-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62197-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62197-score" class="post-score" title="current number of votes">0</div><span id="post-62197-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>how to filter either strings at once ? I wrote something like this:</p><p><strong>-Y "tcp contains "hi"" || tcp contains "bye""</strong></p><p>but it doesnt works, anyone please help? Thanks</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-tshark" rel="tag" title="see questions tagged &#39;tshark&#39;">tshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jun '17, 21:36</strong></p><img src="https://secure.gravatar.com/avatar/4c7f3d4e990f094bdbc580331215ab44?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JJ24&#39;s gravatar image" /><p><span>JJ24</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JJ24 has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>20 Jun '17, 21:37</strong> </span></p></div></div><div id="comments-container-62197" class="comments-container"></div><div id="comment-tools-62197" class="comment-tools"></div><div class="clear"></div><div id="comment-62197-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="62198"></span>

<div id="answer-container-62198" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-62198-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-62198-score" class="post-score" title="current number of votes">0</div><span id="post-62198-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="JJ24 has selected this answer as the correct answer"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>You have to escape the quotes there:</p><pre><code>-Y &quot;tcp contains \&quot;hi\&quot; || tcp contains \&quot;bye\&quot;&quot;</code></pre><p>That should work. The escape tells the operating system that the next character is not to be interpreted but passed "as is" to the application. Without escape, the OS will read from quote to quote and break the parameters. This is valid for any application, you can see the effect by creating a shell script (if Linux) or a batch script (if Windows) and run it with the parameters. Below it captures up to 4 parameters, you can expand as needed.</p><p>Linux:</p><pre><code>echo &quot;1: &#39;$1&#39;, 2: &#39;$2&#39;, 3: &#39;$3&#39;, 4: &#39;$4&#39;&quot;</code></pre><p>Windows:</p><pre><code>echo &quot;1: &#39;%1&#39;, 2: &#39;%2&#39;, 3: &#39;%3&#39;, 4: &#39;%4&#39;&quot;</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Jun '17, 23:21</strong></p><img src="https://secure.gravatar.com/avatar/ae9b5fba493daf2baf29a681f99e7418?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="silvio&#39;s gravatar image" /><p><span>silvio</span><br />
<span class="score" title="31 reputation points">31</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="silvio has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p><span> edited <strong>21 Jun '17, 08:05</strong> </span></p></div></div><div id="comments-container-62198" class="comments-container"></div><div id="comment-tools-62198" class="comment-tools"></div><div class="clear"></div><div id="comment-62198-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

