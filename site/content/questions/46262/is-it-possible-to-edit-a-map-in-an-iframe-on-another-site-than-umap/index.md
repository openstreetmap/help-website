+++
type = "question"
title = "Is it possible to edit a map in an iframe on another site than umap?"
description = '''Hello everyone, Even though my map is set to allow anyone to edit, and I can actually edit it anonymously on umap.openstreetmap.fr, whenever I&#x27;m trying to edit it in an iframe on another website where it&#x27;s embedded, I get this error: &quot;action not allowed&quot; (translated from french). I get the error onl...'''
date = "2015-10-31T01:22:00Z"
lastmod = "2015-10-31T21:45:00Z"
weight = 46262
keywords = [ "umap", "editing", "public", "iframe" ]
aliases = [ "/questions/46262" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Is it possible to edit a map in an iframe on another site than umap?](/questions/46262/is-it-possible-to-edit-a-map-in-an-iframe-on-another-site-than-umap)

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
<span id="post-46262-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46262-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46262-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone, Even though my map is set to allow anyone to edit, and I can actually edit it anonymously on umap.openstreetmap.fr, whenever I'm trying to edit it in an iframe on another website where it's embedded, I get this error: "action not allowed" (translated from french). I get the error only when saving changes.</p>
<p>And I have to say that the website where the map is embedded is accessed localy, but it does access the internet to display the map with no issue. So my website is actually only <a href="http://localhost">http://localhost</a></p>
<p>Is this error normal or should I be able to anonymously edit this map? Here it is: <a href="https://umap.openstreetmap.fr/fr/map/grenoble-libre-edition_58385">https://umap.openstreetmap.fr/fr/map/grenoble-libre-edition_58385</a></p>
<p>I hope someone could enlighten me...</p>
<p><strong>Edit:</strong> Here is a picture of the error after creating a new marker and trying to save it in the iframe <img src="/upfiles/iframe_error.jpg" alt="alt text" /></p>
<p><strong>Edit 2:</strong> Here are the iframe element parameters (I removed the first iframe tag because it wouldn't display the code correctly):</p>
<pre><code>width=&quot;980px&quot; height=&quot;550px&quot; frameBorder=&quot;0&quot; src=&quot;https://umap.openstreetmap.fr/fr/map/grenoble-libre-edition_58385?scaleControl=true&amp;miniMap=true&amp;scrollWheelZoom=true&amp;zoomControl=true&amp;allowEdit=true&amp;moreControl=false&amp;datalayersControl=false&amp;onLoadPanel=undefined&amp;captionBar=false&amp;editInOSMControl=true&quot;&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-umap" rel="tag" title="see questions tagged &#39;umap&#39;">umap</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-public" rel="tag" title="see questions tagged &#39;public&#39;">public</span> <span class="post-tag tag-link-iframe" rel="tag" title="see questions tagged &#39;iframe&#39;">iframe</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '15, 01:22</strong></p>
<img src="https://secure.gravatar.com/avatar/60731d9ed48de1b1fbc8c870ba54b086?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="racco&#39;s gravatar image" />
<p><span>racco</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="racco has no accepted answers">0%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '15, 11:21</strong> </span></p>
</div>
</div>
<div id="comments-container-46262" class="comments-container">
<span id="46268"></span>
<div id="comment-46268" class="comment">
<div id="post-46268-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am not sure if I understand correctly (maybe a screenshot of your error would help). Can you do your edits in the iframe but then saving results in an error?</p>
<p>In the iframe code <em>generated by umap</em> there is a HTTP GET parameter "allowEdit" which is set to "false". Set it it to "true" and try again. So, this: <a href="https://umap.openstreetmap.fr/fr/map/grenoble-libre-edition_58385?miniMap=false&amp;scrollWheelZoom=false&amp;zoomControl=true&amp;allowEdit=true&amp;moreControl=true&amp;datalayersControl=true&amp;onLoadPanel=undefined&amp;captionBar=false#14/45.1928/5.7340">https://umap.openstreetmap.fr/fr/map/grenoble-libre-edition_58385?miniMap=false&amp;scrollWheelZoom=false&amp;zoomControl=true&amp;allowEdit=true&amp;moreControl=true&amp;datalayersControl=true&amp;onLoadPanel=undefined&amp;captionBar=false#14/45.1928/5.7340</a></p>
<p>But this just controls the UI elements for editing, if you can do edits but just not save, then this is <em>not your issue</em></p>
</div>
<div id="comment-46268-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 10:07)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="46270"></span>
<div id="comment-46270" class="comment">
<div id="post-46270-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>that's right, I can do my edits in the iframe, but when saving it says "action not allowed with a red bar. I added a screenshot as you suggested. And also setting "scaleControl" to "true" as suggested doesn't help ...</p>
</div>
<div id="comment-46270-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 11:01)</span> <span class="comment-user userinfo">racco</span>
</div>
</div>
<span id="46271"></span>
<div id="comment-46271" class="comment">
<div id="post-46271-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks for your answer. unfortunatly setting the "scaleControl" parameter to "true" in the iframe doesn't solve the problem. Your exemple link still has "scaleControl" set to "false" by the way ;) I added my iframe code in the OP too.</p>
</div>
<div id="comment-46271-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 11:04)</span> <span class="comment-user userinfo">racco</span>
</div>
</div>
<span id="46279"></span>
<div id="comment-46279" class="comment">
<div id="post-46279-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/11634/racco">@racco</a>: sorry, I copied the wrong one, I meant "allowEdit"</p>
</div>
<div id="comment-46279-info" class="comment-info">
<span class="comment-age">(31 Oct '15, 21:45)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46262" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46262-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

