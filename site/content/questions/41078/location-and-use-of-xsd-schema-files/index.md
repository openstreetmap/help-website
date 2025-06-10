+++
type = "question"
title = "location and use of .xsd Schema files?"
description = '''(q1) Where is the official source of the current OSM .xsd Schema file?  Checked the Wiki and found this page as a start: http://wiki.openstreetmap.org/wiki/OSM_XML/XSD Is that it? (q2) How do you modify the xml Export (.osm) file to reference the authoritative .xsd Schema file? (Note: export writes ...'''
date = "2015-02-17T14:23:00Z"
lastmod = "2015-02-17T17:07:00Z"
weight = 41078
keywords = [ "osm-file_format", "namespace", ".osm", "xsd", "schema" ]
aliases = [ "/questions/41078" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [location and use of .xsd Schema files?](/questions/41078/location-and-use-of-xsd-schema-files)

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
<span id="post-41078-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41078-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-41078-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p><strong>(q1) Where is the official source of the current OSM .xsd Schema file?</strong></p>
<p>Checked the Wiki and found this page as a start: <a href="http://wiki.openstreetmap.org/wiki/OSM_XML/XSD">http://wiki.openstreetmap.org/wiki/OSM_XML/XSD</a> Is that it?</p>
<p><strong>(q2) How do you modify the xml Export (.osm) file to reference the authoritative .xsd Schema file?</strong></p>
<p>(Note: export writes a .osm file which is XML, and can easily be renamed to .xml)</p>
<p>Speculate you just take line 2 of the .xml file which contains this:</p>
<pre><code> osm version=... generator=... copyright=... attribution=... license=...</code></pre>
<p>and add in ( ahead of the closing "&gt;" )</p>
<pre><code> xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot;</code></pre>
<p>and</p>
<pre><code> xsi:noNamespaceSchemaLocation=&quot;OSMSchema.xsd&quot;</code></pre>
<p>Provided you have a validated copy of the current OSM .xsd file named <code>OSMSchema.xsd</code> and its located in the same directory.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm-file_format" rel="tag" title="see questions tagged &#39;osm-file_format&#39;">osm-file_format</span> <span class="post-tag tag-link-namespace" rel="tag" title="see questions tagged &#39;namespace&#39;">namespace</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-xsd" rel="tag" title="see questions tagged &#39;xsd&#39;">xsd</span> <span class="post-tag tag-link-schema" rel="tag" title="see questions tagged &#39;schema&#39;">schema</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '15, 14:23</strong></p>
<img src="https://secure.gravatar.com/avatar/8013aaefe8421cedc8ab429b1ed0aa62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rjl&#39;s gravatar image" />
<p><span>rjl</span><br />
<span class="score" title="30 reputation points">30</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rjl has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-41078" class="comments-container">
<span id="41079"></span>
<div id="comment-41079" class="comment">
<div id="post-41079-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Can you explain in a little more detail what it is that you are actually trying to do?</p>
</div>
<div id="comment-41079-info" class="comment-info">
<span class="comment-age">(17 Feb '15, 14:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="41080"></span>
<div id="comment-41080" class="comment">
<div id="post-41080-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Trying to get .osm to load and validate against authoritative .xsd . OSMSchema.xsd (that I found) has xmlns="http://openstreetmap.org/osm/0.6" and targetNamespace="http://openstreetmap.org/osm/0.6" yet .osm files don't utilize a namespace? Project otherwise seems quite mature.</p>
</div>
<div id="comment-41080-info" class="comment-info">
<span class="comment-age">(17 Feb '15, 15:08)</span> <span class="comment-user userinfo">rjl</span>
</div>
</div>
<span id="41082"></span>
<div id="comment-41082" class="comment">
<div id="post-41082-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This doesn't seem to be a question, or if so is largely rhetorical. Consider rephrasing it, and adding information about why you want to ask the question.</p>
</div>
<div id="comment-41082-info" class="comment-info">
<span class="comment-age">(17 Feb '15, 15:36)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="41083"></span>
<div id="comment-41083" class="comment">
<div id="post-41083-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>XML files are not required to contain namespace declarations.</p>
</div>
<div id="comment-41083-info" class="comment-info">
<span class="comment-age">(17 Feb '15, 15:37)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-41078" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41078-form-container" class="comment-form-container">
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

<span id="41085"></span>

<div id="answer-container-41085" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-41085-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-41085-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-41085-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="rjl has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is no official xsd schema file, which is why it doesn't appear referenced from within the files.</p>
<p>There's no official schema in any other format either.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '15, 15:41</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-41085" class="comments-container">
<span id="41090"></span>
<div id="comment-41090" class="comment">
<div id="post-41090-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks. Good to know.</p>
</div>
<div id="comment-41090-info" class="comment-info">
<span class="comment-age">(17 Feb '15, 17:07)</span> <span class="comment-user userinfo">rjl</span>
</div>
</div>
</div>
<div id="comment-tools-41085" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-41085-form-container" class="comment-form-container">
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

