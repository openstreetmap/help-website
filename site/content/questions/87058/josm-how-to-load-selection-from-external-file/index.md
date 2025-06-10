+++
type = "question"
title = "JOSM: How to load selection from external file?"
description = '''Hello, All. I&#x27;m using JOSM (Revision:18583 Build-Date:2022-11-01 14:35:40) on windows-64, and try to load selection from an external file, but with no luck. :-( Help says that there is a possibility to use urls in the search prompt for such files:  Fetch external file and replace selection A very un...'''
date = "2023-04-05T08:02:00Z"
lastmod = "2023-04-06T16:57:00Z"
weight = 87058
keywords = [ "josm", "selection" ]
aliases = [ "/questions/87058" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [JOSM: How to load selection from external file?](/questions/87058/josm-how-to-load-selection-from-external-file)

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
<span id="post-87058-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87058-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87058-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, All. I'm using JOSM (Revision:18583 Build-Date:2022-11-01 14:35:40) on windows-64, and try to load selection from an external file, but with no luck. :-(</p>
<p>Help says that there is a possibility to use urls in the search prompt for such files:</p>
<blockquote>
<p><strong>Fetch external file and replace</strong> selection A very under-used feature that lets you enter a web URL (file://, http://, https://, ftp://) in the search field. JOSM will then attempt to load that URL, and select any objects that it finds referenced in that file. JOSM will look for XML tags "way", "node", and "relation" in the document (clarify? examples?), and use their id attribute . You can access another OSM file on your hard disk this way and have JOSM select all objects that are present in the file (provided they are present in JOSM's dataset too).</p>
</blockquote>
<p>The help is very vague on the subject. I've tried this with a <em>"file://drive/path/file.ext"</em> url, and even run an http server and used a <em>"http://localhost/found-outlines.xml"</em> url. And I've tried different file formats, like "wNNNNNNN", "&lt;way id="NNNNNN"&gt;&lt;/way&gt;" per line. Also nothing happens if I use standard osm (xml) file.</p>
<p>Did anyone make it working? How must the data to be formatted in the file, and how to give the url to the file correctly? Maybe it's disabled somewhere in the preferences?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-selection" rel="tag" title="see questions tagged &#39;selection&#39;">selection</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 Apr '23, 08:02</strong></p>
<img src="https://secure.gravatar.com/avatar/10473a741c2a94803c357db1466a8d80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mechanic_ua&#39;s gravatar image" />
<p><span>mechanic_ua</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mechanic_ua has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 Apr '23, 08:04</strong> </span></p>
</div>
</div>
<div id="comments-container-87058" class="comments-container">
<span id="87059"></span>
<div id="comment-87059" class="comment">
<div id="post-87059-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Why are you trying to load an OSM file from a URL rather than just using File&gt;Open ?</p>
<p>I've not spent much time manually editing OSM files but I would expect a way to require reference to nodes between the open and close tags too.</p>
<p>This question sounds like there is background that would be useful. What are you <em>actually</em> trying to do?</p>
</div>
<div id="comment-87059-info" class="comment-info">
<span class="comment-age">(05 Apr '23, 09:44)</span> <span class="comment-user userinfo">InsertUser</span>
</div>
</div>
<span id="87060"></span>
<div id="comment-87060" class="comment">
<div id="post-87060-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm not trying to <em>open data</em> with url, the data is already opened in editor. All I need is to load <em>selection</em> (select elements by an externally passed list of IDs). Those IDs I get from my own scripts, which fiddle with SQL queries to somehow process them. Actually I'm building a workflow to generate 3d city with as much existing data as I can collect. Some data is my-project-only-related, so there is no sense to clutter a global database with it. But I use osm objects' IDs to sync my own data among my tools. JOSM is a very handy tool to edit spatial data visually, and it's easy to generate it's format (xml) for data exchange. Multiple selection is mostly for merging layers with "merge selection" command. I know about remote control, but it would be more convenient to feed a long lists of id's directly from texts. I'd already started to invent the wheel, but someone has dropped those few lines in the help, which somehow stops me from reinventing an already existing (?) wheel :-) If it works, I need to know how, and if it doesn't, then nothing will stop me from facing a shiny brand new wheel. =)</p>
</div>
<div id="comment-87060-info" class="comment-info">
<span class="comment-age">(05 Apr '23, 11:40)</span> <span class="comment-user userinfo">mechanic_ua</span>
</div>
</div>
</div>
<div id="comment-tools-87058" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87058-form-container" class="comment-form-container">
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

<span id="87070"></span>

<div id="answer-container-87070" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87070-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you, All. You helped a lot just doing nothing! ;-) While the question were itching, I decided to get my paws dirty with the JOSM source. At last. And now I can just build it, set some breakpoints, and trace whatever I cannot understand in the help system.</p>
<p><strong>The right answer to my question is "Nope".</strong> :-|</p>
<p>No, there is no search string hooks in the last release of JOSM which will do something like that mentioned in the help. And yes, it just parses the url into the pair <code>key='http', value='//localhost/file.xml'</code>. This pair is used as the search settings in <code>org.openstreetmap.josm.actions.search.SearchAction.SearchTask.realRun()</code>.</p>
<p>So, magic doesn't live in this code, just in the help..</p>
<p>Hope, that someone won't believe me, and will compile his own custom jar oneself! ;-)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Apr '23, 16:57</strong></p>
<img src="https://secure.gravatar.com/avatar/10473a741c2a94803c357db1466a8d80?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mechanic_ua&#39;s gravatar image" />
<p><span>mechanic_ua</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mechanic_ua has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87070" class="comments-container">
&#10;</div>
<div id="comment-tools-87070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87070-form-container" class="comment-form-container">
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

