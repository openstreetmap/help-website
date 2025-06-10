+++
type = "question"
title = "JSONDecodeError when convert query result in jupyter notebook (python)"
description = '''Hello, I&#x27;m using python (jupyter notebook) to get data of hospitals in Bali area, Indonesia. Here is my code and query: import pandas as pd import requests import json overpass_api = &quot;http://overpass-api.de/api/interpreter&quot;  query_hospital = &quot;&quot;&quot; [out:json]; {{geocodeArea:&#x27;Provinsi Bali&#x27;}}-&amp;gt;.searc...'''
date = "2022-05-08T15:05:00Z"
lastmod = "2022-05-09T23:41:00Z"
weight = 84408
keywords = [ "python", "query", "json", "jupyter" ]
aliases = [ "/questions/84408" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JSONDecodeError when convert query result in jupyter notebook (python)](/questions/84408/jsondecodeerror-when-convert-query-result-in-jupyter-notebook-python)

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
<span id="post-84408-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84408-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84408-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm using python (jupyter notebook) to get data of hospitals in Bali area, Indonesia. Here is my code and query:</p>
<pre><code>import pandas as pd
import requests
import json
overpass_api = &quot;http://overpass-api.de/api/interpreter&quot;
&#10;query_hospital = &quot;&quot;&quot;
[out:json];
{{geocodeArea:&#39;Provinsi Bali&#39;}}-&gt;.searchArea;
node[amenity=&#39;hospital&#39;](area.searchArea);
out;
&quot;&quot;&quot;
&#10;response_hospital = requests.get(overpass_api, params={&#39;data&#39;:query_hospital})</code></pre>
<p>but when I run the next code,</p>
<pre><code>data_hospital = response_hospital.json()</code></pre>
<p>it returns error <code>JSONDecodeError: Expecting value: line 1 column 1 (char 0)</code></p>
<p>the query works well in <a href="https://overpass-turbo.eu/">Overpass Turbo</a> but when I put in notebook, it returns error.</p>
<p>Thanks for the help.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-query" rel="tag" title="see questions tagged &#39;query&#39;">query</span> <span class="post-tag tag-link-json" rel="tag" title="see questions tagged &#39;json&#39;">json</span> <span class="post-tag tag-link-jupyter" rel="tag" title="see questions tagged &#39;jupyter&#39;">jupyter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '22, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/95960c4ea8f9bf17c54226dc5c596bfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="salmiah-ls&#39;s gravatar image" />
<p><span>salmiah-ls</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="salmiah-ls has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 May '22, 23:43</strong> </span></p>
</div>
</div>
<div id="comments-container-84408" class="comments-container">
<span id="84413"></span>
<div id="comment-84413" class="comment">
<div id="post-84413-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>check the status code of the query, it's returning 400. The <code>.text</code> says: <code>Error: line 2: parse error: Unknown type "{"</code>, <code>Error: line 2: parse error: An empty query is not allowed</code> and <code>Error: line 2: parse error: ';' expected - '{' found.</code></p>
</div>
<div id="comment-84413-info" class="comment-info">
<span class="comment-age">(08 May '22, 20:31)</span> <span class="comment-user userinfo">Marcos Dione</span>
</div>
</div>
<span id="84414"></span>
<div id="comment-84414" class="comment">
<div id="post-84414-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>yes, I have the same thought. looks like python can't parse that double curly braces {{ }}.</p>
<p>I wonder if there is way to modify the query in OSM so it can return the same result but without that double curly braces.</p>
</div>
<div id="comment-84414-info" class="comment-info">
<span class="comment-age">(09 May '22, 05:53)</span> <span class="comment-user userinfo">salmiah-ls</span>
</div>
</div>
</div>
<div id="comment-tools-84408" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84408-form-container" class="comment-form-container">
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

<span id="84422"></span>

<div id="answer-container-84422" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84422-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84422-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84422-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've found the solution.</p>
<p>I modify the query so I doesn't include the double curly braces {{ }} anymore, which seems python can't parse. Here is my new query:</p>
<pre><code>query_hospital = &quot;&quot;&quot;
[out:json];
area[name=Bali];
node[amenity=&#39;hospital&#39;](area);
out;
&quot;&quot;&quot;</code></pre>
<p>or if we use area name in local language:</p>
<pre><code>query_hospital = &quot;&quot;&quot;
[out:json];
area[&#39;name:id&#39;=&#39;Provinsi Bali&#39;];
node[amenity=&#39;hospital&#39;](area);
out;
&quot;&quot;&quot;</code></pre>
<p>the query returns same result and python can parse it now.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '22, 23:41</strong></p>
<img src="https://secure.gravatar.com/avatar/95960c4ea8f9bf17c54226dc5c596bfe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="salmiah-ls&#39;s gravatar image" />
<p><span>salmiah-ls</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="salmiah-ls has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 May '22, 23:57</strong> </span></p>
</div>
</div>
<div id="comments-container-84422" class="comments-container">
&#10;</div>
<div id="comment-tools-84422" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84422-form-container" class="comment-form-container">
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

