+++
type = "question"
title = "Missing house numbers after TIGER import on local Nominatim instance"
description = '''I&#x27;ve had a look through some of the existing questions on this, and I can&#x27;t quite find anything that matches. I&#x27;m running a local instance of Nominatim 3.4.1 and the results that I&#x27;m getting are missing the house numbers, despite having imported the TIGER data. The test case that I&#x27;m using is &quot;2037 ...'''
date = "2020-01-29T22:16:00Z"
lastmod = "2020-01-29T22:16:00Z"
weight = 72762
keywords = [ "tiger", "housenumbers" ]
aliases = [ "/questions/72762" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Missing house numbers after TIGER import on local Nominatim instance](/questions/72762/missing-house-numbers-after-tiger-import-on-local-nominatim-instance)

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
<span id="post-72762-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-72762-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-72762-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've had a look through some of the existing questions on this, and I can't quite find anything that matches.</p>
<p>I'm running a local instance of Nominatim 3.4.1 and the results that I'm getting are missing the house numbers, despite having imported the TIGER data.</p>
<p>The test case that I'm using is "2037 Goldfield Ln", which should return an address in Sonoma County, California.</p>
<p>As per the CentOS instructions I downloaded, extracted and then loaded the TIGER data as follows:</p>
<p>./utils/setup.php --import-tiger-data ./utils/setup.php --create-functions --enable-diff-updates --create-partition-functions</p>
<p>Before running the second command, I verified that CONST_Use_US_Tiger_Data (sorry, the underscores are messing with the formatting) was set in ./settings/local.php within my build directory.</p>
<p>However when I search using my test case, the house number is not being returned from my local instance.</p>
<p>Does anyone have any suggestions as to what might be going wrong, or if there's some step that I've missed?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiger" rel="tag" title="see questions tagged &#39;tiger&#39;">tiger</span> <span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '20, 22:16</strong></p>
<img src="https://secure.gravatar.com/avatar/7663d27b40f7373f22e3f997a3714365?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="William&#39;s gravatar image" />
<p><span>William</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="William has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-72762" class="comments-container">
&#10;</div>
<div id="comment-tools-72762" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-72762-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

