+++
type = "question"
title = "how  can i convert GPS tracer to json file"
description = '''Hi  I&#x27;m trying to using the API to extract the GPS Tracer, and I would like to dump it into a JSON file  I used the following code: #overpass api url url = &#x27;https://api.openstreetmap.org/api/0.6/trackpoints?bbox=0,51.5,0.25,51.75&amp;amp;page=0&#x27; response = requests.get(url) response.json()  but unfortun...'''
date = "2021-03-13T11:29:00Z"
lastmod = "2021-03-15T08:25:00Z"
weight = 79245
keywords = [ "openstreetmap", "gps-traces", "gpx" ]
aliases = [ "/questions/79245" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [how can i convert GPS tracer to json file](/questions/79245/how-can-i-convert-gps-tracer-to-json-file)

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
<span id="post-79245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-79245-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-79245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi I'm trying to using the API to extract the GPS Tracer, and I would like to dump it into a JSON file I used the following code:</p>
<pre><code>#overpass api url
url = &#39;https://api.openstreetmap.org/api/0.6/trackpoints?bbox=0,51.5,0.25,51.75&amp;page=0&#39;
response = requests.get(url)
response.json()</code></pre>
<p>but unfortunately, this code gives me this error</p>
<blockquote>
<p>JSONDecodeError: Expecting value: line 1 column 1 (char 0)</p>
</blockquote>
<p>is it possible to convert it to JSON format?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-gps-traces" rel="tag" title="see questions tagged &#39;gps-traces&#39;">gps-traces</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Mar '21, 11:29</strong></p>
<img src="https://secure.gravatar.com/avatar/00b20ea2eb5708a716896e0d335050f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rabeeqasem&#39;s gravatar image" />
<p><span>rabeeqasem</span><br />
<span class="score" title="31 reputation points">31</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rabeeqasem has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-79245" class="comments-container">
<span id="79254"></span>
<div id="comment-79254" class="comment">
<div id="post-79254-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This URL returns GPX. You need a GPX-to-JSON converter.</p>
</div>
<div id="comment-79254-info" class="comment-info">
<span class="comment-age">(15 Mar '21, 08:25)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-79245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-79245-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

