+++
type = "question"
title = "Cannot get mapnik image from export/finish with Python"
description = '''I want to get image from &quot;http://www.openstreetmap.org/export/finish&quot; or &quot;http://api06.dev.openstreetmap.org/export/finish&quot; with Python. I tried this command. import requests  url = &quot;http://www.openstreetmap.org/export/finish&quot; &amp;lt;br /&amp;gt; r = requests.post(url,{&#x27;mapnik_format&#x27;: &#x27;png&#x27;, &#x27;minlon&#x27;: 135...'''
date = "2017-01-04T05:35:00Z"
lastmod = "2017-03-29T22:38:00Z"
weight = 53853
keywords = [ "python", "export", "mapnik", "error" ]
aliases = [ "/questions/53853" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Cannot get mapnik image from export/finish with Python](/questions/53853/cannot-get-mapnik-image-from-exportfinish-with-python)

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
<span id="post-53853-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53853-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53853-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get image from "http://www.openstreetmap.org/export/finish" or "http://api06.dev.openstreetmap.org/export/finish" with Python.</p>
<p>I tried this command.</p>
<pre><code>import requests
&#10;url = &quot;http://www.openstreetmap.org/export/finish&quot; &lt;br /&gt;
r = requests.post(url,{&#39;mapnik_format&#39;: &#39;png&#39;, &#39;minlon&#39;: 135.74, &#39;minlat&#39;: 35.011, &#39;maxlon&#39;: 135.75, &#39;maxlat&#39;: 35.014, &#39;format&#39;: &#39;mapnik&#39;, &#39;mapnik_scale&#39;: 30000})</code></pre>
<p>but r is Response [400] and r.content is this</p>
<pre><code>&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Error&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Error&lt;/h1&gt;
&lt;p&gt;Missing or invalid token&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
<p>Why I can't get image? How should I do?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '17, 05:35</strong></p>
<img src="https://secure.gravatar.com/avatar/c2c6c51a1d9bde0ffbc59dbc25a00f8b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="taki_&#39;s gravatar image" />
<p><span>taki_</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="taki_ has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Jan '17, 07:59</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-53853" class="comments-container">
&#10;</div>
<div id="comment-tools-53853" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53853-form-container" class="comment-form-container">
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

<span id="53859"></span>

<div id="answer-container-53859" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53859-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53859-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53859-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The export facility on the web site is not meant to be used programmatically. (See <a href="https://operations.osmfoundation.org/policies/tiles/">https://operations.osmfoundation.org/policies/tiles/</a> which says "Calls to /cgi-bin/export may only be triggered by direct end-user action." - even though you're not calling /cgi-bin/export this is the same thing.)</p>
<p>So even if the problem you are seeing could be fixed, you'd be using the interface in disregard of the policy.</p>
<p>Generally the best and most reliable way to generate static map images is to run your own rendering server - that way you can make as many requests as you like and you're not killing anyone else's server with it. If you absolutely must use a hosted service, have a look at <a href="http://wiki.openstreetmap.org/wiki/Static_map_images">http://wiki.openstreetmap.org/wiki/Static_map_images</a> but be aware that the services listed there are not suitable for massive use either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>04 Jan '17, 09:53</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-53859" class="comments-container">
<span id="53969"></span>
<div id="comment-53969" class="comment">
<div id="post-53969-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, I see. Thank you.</p>
</div>
<div id="comment-53969-info" class="comment-info">
<span class="comment-age">(10 Jan '17, 13:19)</span> <span class="comment-user userinfo">taki_</span>
</div>
</div>
<span id="55345"></span>
<div id="comment-55345" class="comment">
<div id="post-55345-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, the same error occurs from the web gui when trying to export a page, to any format.</p>
</div>
<div id="comment-55345-info" class="comment-info">
<span class="comment-age">(29 Mar '17, 22:38)</span> <span class="comment-user userinfo">quazgar</span>
</div>
</div>
</div>
<div id="comment-tools-53859" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53859-form-container" class="comment-form-container">
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

