+++
type = "question"
title = "osm2pgsql tablespaces on SSDs."
description = '''Hello,  I&#x27;m not sure if this is a simple question with a straightforward answer, but I&#x27;ll ask anyway. I know for spinning HDDs splitting the tablespaces across multiple drives has been shown to increase performance when loading the planet file into postgres using osm2pgsql, but what about SSDs? All ...'''
date = "2016-05-08T03:01:00Z"
lastmod = "2016-05-08T03:01:00Z"
weight = 49617
keywords = [ "hardware", "import", "benchmark", "osm2pgsql" ]
aliases = [ "/questions/49617" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [osm2pgsql tablespaces on SSDs.](/questions/49617/osm2pgsql-tablespaces-on-ssds)

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
<span id="post-49617-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49617-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-49617-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm not sure if this is a simple question with a straightforward answer, but I'll ask anyway.</p>
<p>I know for spinning HDDs splitting the tablespaces across multiple drives has been shown to increase performance when loading the planet file into postgres using osm2pgsql, but what about SSDs?</p>
<p>All things being equal, which of the following options is faster (or more efficient) when farming out the 4 osm2pgsql tablespaces (i.e. main_data, main_index, slim_data, and slim_index):</p>
<ol>
<li>a single large (1TB) SSD with 1 partition.</li>
<li>a single large (1TB) SSD with 4 partitions (one for each tablespace).</li>
<li>2 medium sized (512GB) SSDs (one for data and one for indices).</li>
<li>4 smaller (&lt;=512GB) SSDs (one for each tablespace).</li>
<li>Maybe some other configuration?</li>
</ol>
<p>I have a 1TB SSD I can test option 1 and 2 with, but if options 3 and/or 4 are not any faster, I'd rather not spend the money to find out.</p>
<p>Has anyone benchmarked this?</p>
<p>Thanks,</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hardware" rel="tag" title="see questions tagged &#39;hardware&#39;">hardware</span> <span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-benchmark" rel="tag" title="see questions tagged &#39;benchmark&#39;">benchmark</span> <span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '16, 03:01</strong></p>
<img src="https://secure.gravatar.com/avatar/487645f035e9b2f095acf7510b32ce89?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="placebo10&#39;s gravatar image" />
<p><span>placebo10</span><br />
<span class="score" title="71 reputation points">71</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="placebo10 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-49617" class="comments-container">
&#10;</div>
<div id="comment-tools-49617" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49617-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

