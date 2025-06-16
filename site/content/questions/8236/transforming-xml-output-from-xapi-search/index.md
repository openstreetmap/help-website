+++
type = "question"
title = "Transforming XML output from XAPI search"
description = '''I want to create a relation for a river. I do a XAPI name tag search and save the XML file in my computer. How do I transform the XML - I need to filter way ids and transform them into XML relation members for input with RawEditor. I have an XSLT stylesheet ready but I have trouble displaying the re...'''
date = "2011-10-02T18:49:00Z"
lastmod = "2011-10-03T14:05:00Z"
weight = 8236
keywords = [ "xml", "stylesheet", "xapi", "relations", "xslt" ]
aliases = [ "/questions/8236" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Transforming XML output from XAPI search](/questions/8236/transforming-xml-output-from-xapi-search)

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
<span id="post-8236-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8236-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-8236-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create a relation for a river. I do a XAPI name tag search and save the XML file in my computer. How do I transform the XML - I need to filter way ids and transform them into XML relation members for input with <a href="https://wiki.openstreetmap.org/wiki/RawEditor">RawEditor</a>. I have an XSLT stylesheet ready but I have trouble displaying the result in Firefox (shows blank page).</p>
<p>The stylesheet is here:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;xsl:stylesheet version=&quot;1.0&quot; xmlns:xsl=&quot;http://www.w3.org/1999/XSL/Transform&quot;&gt;
&lt;xsl:output method=&quot;xml&quot; indent=&quot;yes&quot;/&gt;
&#10;&lt;xsl:template match=&quot;/osm&quot;&gt;
  &lt;relation&gt;
    &lt;xsl:apply-templates select=&quot;way&quot;/&gt;
  &lt;/relation&gt;
&lt;/xsl:template&gt;
&#10;&lt;xsl:template match=&quot;way&quot;&gt;
  &lt;member type=&quot;way&quot; ref=&quot;{@id}&quot;/&gt;
&lt;/xsl:template&gt;
&#10;&lt;/xsl:stylesheet&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-xml" rel="tag" title="see questions tagged &#39;xml&#39;">xml</span> <span class="post-tag tag-link-stylesheet" rel="tag" title="see questions tagged &#39;stylesheet&#39;">stylesheet</span> <span class="post-tag tag-link-xapi" rel="tag" title="see questions tagged &#39;xapi&#39;">xapi</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span> <span class="post-tag tag-link-xslt" rel="tag" title="see questions tagged &#39;xslt&#39;">xslt</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Oct '11, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/7d327873d48d28e563c9ad7259853c35?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kozuch&#39;s gravatar image" />
<p><span>Kozuch</span><br />
<span class="score" title="1720 reputation points"><span>1.7k</span></span><span title="58 badges"><span class="badge1">●</span><span class="badgecount">58</span></span><span title="72 badges"><span class="silver">●</span><span class="badgecount">72</span></span><span title="85 badges"><span class="bronze">●</span><span class="badgecount">85</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kozuch has one accepted answer">8%</span></p>
</div>
</div>
<div id="comments-container-8236" class="comments-container">
&#10;</div>
<div id="comment-tools-8236" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8236-form-container" class="comment-form-container">
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

<span id="8249"></span>

<div id="answer-container-8249" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8249-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8249-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8249-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wouldn't worry about XML transformations, myself - you're just after filling in the list for the rawedit upload, so that's a bunch of lines like:</p>
<pre><code>&lt;member type=&quot;way&quot; ref=&quot;1234&quot; role=&quot;&quot;/&gt;</code></pre>
<p>I'd create a list of ways that you want to use from the XAPI output and then convert into the required "member" list using an editing macro in your favourite text editor. Obviously you'll then need to check the list of omissions and things that shouldn't be in it manually (have a look at the wiki "browserelation" links).</p>
<p>Then, re-order in the order that you want by following EdLoach's answer to <a href="/questions/8197/re-ordering-ways-in-a-relation">this question</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 Oct '11, 13:08</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-8249" class="comments-container">
<span id="8257"></span>
<div id="comment-8257" class="comment">
<div id="post-8257-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just found an XSL processor called <a href="http://saxon.sourceforge.net/">SAXON</a> which works great with the stylesheet. Or is there easier way how to filter the the ways out of a XAPI search result?</p>
</div>
<div id="comment-8257-info" class="comment-info">
<span class="comment-age">(03 Oct '11, 13:43)</span> <span class="comment-user userinfo">Kozuch</span>
</div>
</div>
<span id="8258"></span>
<div id="comment-8258" class="comment">
<div id="post-8258-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>To filter the ways out of an XAPI search result, I'd use "grep" (or "find matching lines" in editor-of-your-choice) myself, but if SAXON works for you, that's great too.</p>
</div>
<div id="comment-8258-info" class="comment-info">
<span class="comment-age">(03 Oct '11, 14:05)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-8249" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8249-form-container" class="comment-form-container">
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

