+++
type = "question"
title = "Error while uploading &quot;osmapi.OsmApi.ApiError: Request failed: 404 - Not Found - b&#x27;&#x27;"
description = '''I&#x27;ve just started to explore Python OSM API and tried to upload a &quot;way&quot; into Open Street Map. import osmapi api = osmapi.OsmApi(api = &quot;https://api06.dev.openstreetmap.org&quot;, username = &quot;*******&quot;, password =******) cs = api.ChangesetCreate() start = api.NodeCreate({&quot;lon&quot;:39.77188512682915,&quot;lat&quot;:40.996...'''
date = "2020-09-04T14:01:00Z"
lastmod = "2020-09-04T14:01:00Z"
weight = 76432
keywords = [ "python", "osmapi_python" ]
aliases = [ "/questions/76432" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error while uploading "osmapi.OsmApi.ApiError: Request failed: 404 - Not Found - b''](/questions/76432/error-while-uploading-osmapiosmapiapierror-request-failed-404-not-found-b)

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
<span id="post-76432-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76432-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76432-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've just started to explore Python OSM API and tried to upload a "way" into Open Street Map. <code>import osmapi api = osmapi.OsmApi(api = "https://api06.dev.openstreetmap.org", username = "*******", password =******) cs = api.ChangesetCreate() start = api.NodeCreate({"lon":39.77188512682915,"lat":40.99645466061746,"visible":True}) stop = api.NodeCreate({"lon":39.77237597107887,"lat":40.99594855924428,"visible":True}) wayPoints = [start["id"], stop["id"]] way = api.WayCreate({"nd":wayPoints ,"visible":True}) api.ChangesetUpload([{"type":"way","action":"create","data":way}]) api.ChangesetClose()</code></p>
<p>After the execution, "Request failed: 404 - Not Found - b" error occurred. Am I doing something wrong or incomplete?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-osmapi_python" rel="tag" title="see questions tagged &#39;osmapi_python&#39;">osmapi_python</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Sep '20, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/d076f455bcdaf25fed94fa8b64d2a3bc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlperTunga&#39;s gravatar image" />
<p><span>AlperTunga</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlperTunga has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76432" class="comments-container">
&#10;</div>
<div id="comment-tools-76432" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76432-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

