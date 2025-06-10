+++
type = "question"
title = "Problem with generate_xmp.py"
description = '''I&#x27;m trying to do the following: ./generate_xml.py osm.xml my_osm.xml --dbname osm --user osm --password my_password --accept-none  And I get: Traceback (most recent call last):  File &quot;./generate_xml.py&quot;, line 204, in &amp;lt;module&amp;gt;  serialize(template_xml,options)  File &quot;./generate_xml.py&quot;, line 80,...'''
date = "2013-02-03T10:31:00Z"
lastmod = "2013-02-03T10:31:00Z"
weight = 19550
keywords = [ "generate_xml.p" ]
aliases = [ "/questions/19550" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with generate_xmp.py](/questions/19550/problem-with-generate_xmppy)

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
<span id="post-19550-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-19550-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-19550-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to do the following:</p>
<pre><code>./generate_xml.py osm.xml my_osm.xml --dbname osm --user osm --password my_password --accept-none</code></pre>
<p>And I get:</p>
<pre><code>Traceback (most recent call last):
  File &quot;./generate_xml.py&quot;, line 204, in &lt;module&gt;
    serialize(template_xml,options)
  File &quot;./generate_xml.py&quot;, line 80, in serialize
    mapnik.load_map(m,xml,True)
RuntimeError: Failed to find font face &#39;&#39; in FontSet &#39;book-fonts&#39;</code></pre>
<p>What am I doing wrong?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-generate_xml.p" rel="tag" title="see questions tagged &#39;generate_xml.p&#39;">generate_xml.p</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>03 Feb '13, 10:31</strong></p>
<img src="https://secure.gravatar.com/avatar/98f6919216423a8d9243fc5a9da4b96b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaguar_sea&#39;s gravatar image" />
<p><span>jaguar_sea</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaguar_sea has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>03 Feb '13, 10:59</strong> </span></p>
</div>
</div>
<div id="comments-container-19550" class="comments-container">
&#10;</div>
<div id="comment-tools-19550" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-19550-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

