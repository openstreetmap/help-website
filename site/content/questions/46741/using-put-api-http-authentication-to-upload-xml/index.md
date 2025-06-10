+++
type = "question"
title = "Using Put api &amp; http authentication to upload xml"
description = ''' how to upload the xml file to add POI? i want to use put api and http authentication. api url http://api06.dev.openstreetmap.org/api/0.6/changeset/create. Can anyone help me to provide c# code for uploading xml file. xml looks like attached image.'''
date = "2015-11-20T07:26:00Z"
lastmod = "2015-11-20T08:22:00Z"
weight = 46741
keywords = [ "put", "xml", "authentication", "upload" ]
aliases = [ "/questions/46741" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Using Put api & http authentication to upload xml](/questions/46741/using-put-api-http-authentication-to-upload-xml)

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
<span id="post-46741-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46741-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46741-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><img src="http://help.openstreetmap.org/upfiles/osm_image_HgX2PyK.jpg" alt="alt text" /> how to upload the xml file to add POI? i want to use put api and http authentication. api url <a href="http://api06.dev.openstreetmap.org/api/0.6/changeset/create.">http://api06.dev.openstreetmap.org/api/0.6/changeset/create.</a> Can anyone help me to provide c# code for uploading xml file. xml looks like attached image.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-put" rel="tag" title="see questions tagged &#39;put&#39;">put</span> <span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-authentication" rel="tag" title="see questions tagged &#39;authentication&#39;">authentication</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Nov '15, 07:26</strong></p>
<img src="https://secure.gravatar.com/avatar/f56d4d8175c3d7e92d227b3bf1e0c11c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Er%20Pawan%20Verma&#39;s gravatar image" />
<p><span>Er Pawan Verma</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Er Pawan Verma has no accepted answers">0%</span></p>
</img>
</div>
</div>
<div id="comments-container-46741" class="comments-container">
<span id="46744"></span>
<div id="comment-46744" class="comment">
<div id="post-46744-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why exactly do you want to use the OSM API directly for uploading changesets instead of using an editor? Your XML document contains lots of errors. For example <em>Name</em> should be <em>name</em> (lowercase), the same applies to <em>website</em> and your <em>addr:</em> tags. Also, <em>PhoneNo.</em> is wrong and should be <em>phone</em> or <em>contact:phone</em> instead. The tags <em>comment</em> and <em>created_by</em> should be attached to the changeset, not to the element!</p>
</div>
<div id="comment-46744-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 08:06)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="46745"></span>
<div id="comment-46745" class="comment">
<div id="post-46745-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Allow me a note of caution:</p>
<p>If you are doing this because you are writing a software that helps people "manage their online visibility" (i.e. some kind of SEO stuff) then please stop right now and don't pursue this further - we have had enough problems with people mass-adding data of questionable value. Among these problems were bad tagging, no respect for already existing data, geocoding from incompatible licenses, and lack of communication (i.e. users adding this data were unwilling or unable to reply when contacted about their edits).</p>
<p>If you are planning any kind of automated data import, you will also be expected to respect our import guidelines as explained here <a href="http://wiki.openstreetmap.org/wiki/Import/Guidelines">http://wiki.openstreetmap.org/wiki/Import/Guidelines</a> which include, among other things, a requirement of discussing things before importing.</p>
<p>Your XML example contains a number of tagging errors that would make the data useless in OpenStreetMap. If you were to upload this, it would likely be removed again, and if you were to upload several items like that, your account would be blocked for violation of import policies.</p>
</div>
<div id="comment-46745-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 08:08)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="46746"></span>
<div id="comment-46746" class="comment">
<div id="post-46746-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>i am making a academic project. i will just use the testing api.</p>
</div>
<div id="comment-46746-info" class="comment-info">
<span class="comment-age">(20 Nov '15, 08:22)</span> <span class="comment-user userinfo">Er Pawan Verma</span>
</div>
</div>
</div>
<div id="comment-tools-46741" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46741-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

