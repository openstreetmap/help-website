+++
type = "question"
title = "error Open failed osmosischange.osc"
description = '''How about, because I get the following error, followed the instructions but I can not continue /srv/nominatim/Nominatim/build$ ./utils/update.php --import-osmosis-all Currently at sequence 2617 (18/05/2020 18:04:47) - 1 indexed &#x27;/home/ubuntu3/.local/bin/pyosmium-get-changes&#x27; --server &#x27;https://downlo...'''
date = "2020-05-21T17:41:00Z"
lastmod = "2020-05-21T19:06:00Z"
weight = 74943
keywords = [ "nominatim", "updates" ]
aliases = [ "/questions/74943" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [error Open failed osmosischange.osc](/questions/74943/error-open-failed-osmosischangeosc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74943-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74943-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74943-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>How about, because I get the following error, followed the instructions but I can not continue</p>
<p>/srv/nominatim/Nominatim/build$ ./utils/update.php --import-osmosis-all Currently at sequence 2617 (18/05/2020 18:04:47) - 1 indexed '/home/ubuntu3/.local/bin/pyosmium-get-changes' --server 'https://download.geofabrik.de/north-america/mexico-updates' --outfile '/srv/nominatim/Nominatim/build/osmosischange.osc' --size 30 '--start-id' 2617 Traceback (most recent call last): File "/home/ubuntu3/.local/bin/pyosmium-get-changes", line 257, in &lt;module&gt; exit(main(sys.argv[1:])) File "/home/ubuntu3/.local/bin/pyosmium-get-changes", line 237, in main outhandler = WriteHandler(options.outfile) RuntimeError: Open failed for '/srv/nominatim/Nominatim/build/osmosischange.osc': Permission denied</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-updates" rel="tag" title="see questions tagged &#39;updates&#39;">updates</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 May '20, 17:41</strong></p>
<img src="https://secure.gravatar.com/avatar/26678041f79fec6b60d7c9834f78c36c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="marianightcrawler&#39;s gravatar image" />
<p><span>marianightcr...</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="marianightcrawler has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-74943" class="comments-container">
&#10;</div>
<div id="comment-tools-74943" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74943-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="74944"></span>

<div id="answer-container-74944" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-74944-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-74944-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-74944-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The script should be run as user 'nominatim'. The error says <code>/home/ubuntu3/.local/bin/pyosmium-get-changes</code> so I think you installed and ran pyosmium as user <code>ubuntu3</code>.</p>
<p>The documentation <a href="http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates">http://nominatim.org/release-docs/latest/admin/Import-and-Update/#updates</a> should be improved. "same user who will later run the updates" isn't clear enough in that context.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 May '20, 19:06</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-74944" class="comments-container">
&#10;</div>
<div id="comment-tools-74944" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-74944-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

