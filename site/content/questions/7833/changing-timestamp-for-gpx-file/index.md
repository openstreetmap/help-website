+++
type = "question"
title = "Changing timestamp for gpx file"
description = '''Hi, i am just trying to change the timestamp for a gpx-file. I import an nmea-file without an date value. So i added the date value with this command: gpsbabel -i nmea,date=&quot;&#x27;.$final_date.&#x27;&quot; -f &quot;&#x27;.$imgfile_tmp.&#x27;&quot; -x track,pack,split=4m,title=&quot;Track-%d%m%Y-%H%M%S&quot; -o gpx -F &quot;&#x27;.$imgfile_tmp.&#x27;.p&quot; After...'''
date = "2011-09-13T13:42:00Z"
lastmod = "2011-09-19T13:16:00Z"
weight = 7833
keywords = [ "date", "gpx", "value", "change" ]
aliases = [ "/questions/7833" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Changing timestamp for gpx file](/questions/7833/changing-timestamp-for-gpx-file)

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
<span id="post-7833-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7833-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7833-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>i am just trying to change the timestamp for a gpx-file. I import an nmea-file without an date value. So i added the date value with this command:</p>
<p>gpsbabel -i nmea,date="'.$final_date.'" -f "'.$imgfile_tmp.'" -x track,pack,split=4m,title="Track-%d%m%Y-%H%M%S" -o gpx -F "'.$imgfile_tmp.'.p"</p>
<p>After this procedure i split the *.p file into 2 or more gpx files.</p>
<p>But now after this i would like to change only the Date of the track. The Timestamps are okay but the date value is wrong. How can i do this?</p>
<p>Thanks a lot for the help.</p>
<p>Cu kami</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-date" rel="tag" title="see questions tagged &#39;date&#39;">date</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-value" rel="tag" title="see questions tagged &#39;value&#39;">value</span> <span class="post-tag tag-link-change" rel="tag" title="see questions tagged &#39;change&#39;">change</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Sep '11, 13:42</strong></p>
<img src="https://secure.gravatar.com/avatar/965d8c17ed1a109bc715ac4eb65e957b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kami&#39;s gravatar image" />
<p><span>kami</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kami has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7833" class="comments-container">
&#10;</div>
<div id="comment-tools-7833" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7833-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="7838"></span>

<div id="answer-container-7838" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7838-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You might find your answer in this previous question :</p>
<p><a href="http://help.openstreetmap.org/questions/2130/gpx-file-no-time-tag">http://help.openstreetmap.org/questions/2130/gpx-file-no-time-tag</a></p>
<p>especially the answer with <code>xmlstarlet</code></p>
<p>Note that OSM doesn't require a correct date value in GPX files. Any date is accepted (in fact, it could work without timestamp but that's another story).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '11, 15:17</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Sep '11, 15:55</strong> </span></p>
</div>
</div>
<div id="comments-container-7838" class="comments-container">
&#10;</div>
<div id="comment-tools-7838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7838-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7839"></span>

<div id="answer-container-7839" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7839-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7839-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7839-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In your case if you just want to change the same date value everywhere that it occurs in the file, a global search-and-replace with a text editor should do the trick. Just open the .gpx file with your editor of choice (even Windows notepad) and "replace all".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Sep '11, 15:47</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-7839" class="comments-container">
&#10;</div>
<div id="comment-tools-7839" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7839-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8014"></span>

<div id="answer-container-8014" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8014-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8014-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8014-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>thanks a lot for the answer. I used sed to change all entry in the gpx-file. works fine.</p>
<p>find /tmp -name "'.$imgfile.'.o" -exec sed -i 's/'1996-01-'.$timsstmp.''/''.$final_date.''/g' {} ;</p>
<p>Thanks a lot.</p>
<p>Cu kami</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Sep '11, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/965d8c17ed1a109bc715ac4eb65e957b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kami&#39;s gravatar image" />
<p><span>kami</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kami has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-8014" class="comments-container">
&#10;</div>
<div id="comment-tools-8014" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8014-form-container" class="comment-form-container">
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

