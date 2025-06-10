+++
type = "question"
title = "Errorneous GPX zip upload"
description = '''I want to upload many gpx files in one zip archive. After uploading I get following message on my email: It looks like your GPX file 2010.zip with the description 2010, Krasnoyarsk kr and the following tags: automobile failed to import. Here&#x27;s the error:  Generic XML parse error XML parser at line 1...'''
date = "2014-02-09T11:40:00Z"
lastmod = "2014-02-11T04:29:00Z"
weight = 30569
keywords = [ "import", "gpx", "upload", "zip" ]
aliases = [ "/questions/30569" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Errorneous GPX zip upload](/questions/30569/errorneous-gpx-zip-upload)

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
<span id="post-30569-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30569-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30569-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to upload many gpx files in one zip archive.</p>
<p>After uploading I get following message on my email:</p>
<pre><code>It looks like your GPX file
2010.zip
with the description
2010, Krasnoyarsk kr
and the following tags:
automobile
failed to import. Here&#39;s the error:
&#10;Generic XML parse error
XML parser at line 1 column 2</code></pre>
<p>I checked all gpx files inside archive with xmllint, and sure that they are parsable. Also I've opened each of them in josm, and they opened and displayed ok.</p>
<p>How can i know which gpx file in uploaded archive is errorneous ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span> <span class="post-tag tag-link-zip" rel="tag" title="see questions tagged &#39;zip&#39;">zip</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Feb '14, 11:40</strong></p>
<img src="https://secure.gravatar.com/avatar/16a5107ca0c722de83e57801d071fe2e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tupka&#39;s gravatar image" />
<p><span>tupka</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tupka has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30569" class="comments-container">
<span id="30570"></span>
<div id="comment-30570" class="comment">
<div id="post-30570-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Did you use it on <a href="http://www.openstreetmap.org/trace/create">http://www.openstreetmap.org/trace/create</a> ?</p>
<p>I don't think it accepts <code>.zip</code> files.</p>
</div>
<div id="comment-30570-info" class="comment-info">
<span class="comment-age">(09 Feb '14, 13:06)</span> <span class="comment-user userinfo">jgpacker</span>
</div>
</div>
<span id="30571"></span>
<div id="comment-30571" class="comment">
<div id="post-30571-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, I use this interface and it accepts zip files - I have succeffully uploaded and imported a couple of archives in the past.</p>
</div>
<div id="comment-30571-info" class="comment-info">
<span class="comment-age">(09 Feb '14, 13:23)</span> <span class="comment-user userinfo">tupka</span>
</div>
</div>
<span id="30572"></span>
<div id="comment-30572" class="comment">
<div id="post-30572-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I also used .zip but this was a year ago or so.<br />
What about zipping just the half of the GPX files, and then the next half of the remaining tracks.... so you have somekind of 'binary search' that guides you to the .GPX that causes the problems?</p>
</div>
<div id="comment-30572-info" class="comment-info">
<span class="comment-age">(09 Feb '14, 17:23)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
<span id="30610"></span>
<div id="comment-30610" class="comment">
<div id="post-30610-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I think it is possible to find out bad file this way. But it is not convinient as I have many gpx archives in addition to 2010.zip which are produce the same bad result on import.</p>
<p>I created a ticket <a href="https://trac.openstreetmap.org/ticket/5115">here</a>, maybe there is a bug in site engine.</p>
</div>
<div id="comment-30610-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 02:58)</span> <span class="comment-user userinfo">tupka</span>
</div>
</div>
<span id="30611"></span>
<div id="comment-30611" class="comment">
<div id="post-30611-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I doubt a "bug in the engine". I upload now and then gzipped gpx files and never got such an error. After having found the erroneous file(s) using the method iii suggested you should be able to found other erroneous files more easily.</p>
</div>
<div id="comment-30611-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 04:29)</span> <span class="comment-user userinfo">malenki</span>
</div>
</div>
</div>
<div id="comment-tools-30569" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30569-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

