+++
type = "question"
title = "Background Working of Overpass Api ? Code behind exe&#x27;s !"
description = '''I am using overpass api in my local machine,and the source folder contains only executable files(Especially cgi-bin/interpreter.exe and bin/osm3s_query.exe), All i want to know is how these exe&#x27;s work in querying my request. Summary of what i want to know : the code in those exe&#x27;s,how it&#x27;s able to q...'''
date = "2016-01-12T11:38:00Z"
lastmod = "2016-01-13T14:40:00Z"
weight = 47471
keywords = [ "code", "overpass-api" ]
aliases = [ "/questions/47471" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Background Working of Overpass Api ? Code behind exe's !](/questions/47471/background-working-of-overpass-api-code-behind-exes)

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
<span id="post-47471-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-47471-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-47471-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am using overpass api in my local machine,and the source folder contains only executable files(Especially cgi-bin/interpreter.exe and bin/osm3s_query.exe), All i want to know is how these exe's work in querying my request.</p>
<p>Summary of what i want to know : the code in those exe's,how it's able to query in the $DB_DIR :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-code" rel="tag" title="see questions tagged &#39;code&#39;">code</span> <span class="post-tag tag-link-overpass-api" rel="tag" title="see questions tagged &#39;overpass-api&#39;">overpass-api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jan '16, 11:38</strong></p>
<img src="https://secure.gravatar.com/avatar/dfcf9d391ca68ff816e8f9f8ec9f3fc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arun%20Gowtham&#39;s gravatar image" />
<p><span>Arun Gowtham</span><br />
<span class="score" title="0 reputation points">0</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arun Gowtham has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-47471" class="comments-container">
<span id="47472"></span>
<div id="comment-47472" class="comment">
<div id="post-47472-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The source code for Overpass API can be found at <a href="https://github.com/drolbr/Overpass-API">GitHub</a>, is this what you are looking for?</p>
</div>
<div id="comment-47472-info" class="comment-info">
<span class="comment-age">(12 Jan '16, 11:46)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="47473"></span>
<div id="comment-47473" class="comment">
<div id="post-47473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/158/scai">@scai</a> no not this, i need the code behind those exe's to which am sending the query.</p>
</div>
<div id="comment-47473-info" class="comment-info">
<span class="comment-age">(12 Jan '16, 11:48)</span> <span class="comment-user userinfo">Arun Gowtham</span>
</div>
</div>
<span id="47474"></span>
<div id="comment-47474" class="comment">
<div id="post-47474-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>These binaries are build using the code I mentioned above. <em>osm3s_query.exe</em> is build from <a href="https://github.com/drolbr/Overpass-API/blob/master/src/overpass_api/dispatch/osm3s_query.cc">osm3s_query.cc</a>. However I couldn't the source for <em>interpreter.exe</em> probably due to some Makefile magic.</p>
</div>
<div id="comment-47474-info" class="comment-info">
<span class="comment-age">(12 Jan '16, 12:16)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="47483"></span>
<div id="comment-47483" class="comment">
<div id="post-47483-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>The <code>interpreter</code> binary is being built based on the following Makefile.am snippet: <a href="https://github.com/drolbr/Overpass-API/blob/master/src/Makefile.am#L137-L138">https://github.com/drolbr/Overpass-API/blob/master/src/Makefile.am#L137-L138</a> - apart from that there's really very little information available about the inner workings. It's all about: use the force, read the source and ask some questions on the Overpass Dev list if you're stuck.</p>
</div>
<div id="comment-47483-info" class="comment-info">
<span class="comment-age">(12 Jan '16, 15:05)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="47484"></span>
<div id="comment-47484" class="comment">
<div id="post-47484-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>One thing I forgot: maybe should mention what kind of issue you're trying to solve in the first place. That could save you some days or even weeks of digging through the sources.</p>
</div>
<div id="comment-47484-info" class="comment-info">
<span class="comment-age">(12 Jan '16, 15:11)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="47487"></span>
<div id="comment-47487" class="comment not_top_scorer">
<div id="post-47487-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a> am not facing any issue,i just wanted to know how interpreter is processing my input i.e how is my query executed on a directory($DB_DIR) rather than a database !!</p>
</div>
<div id="comment-47487-info" class="comment-info">
<span class="comment-age">(13 Jan '16, 03:57)</span> <span class="comment-user userinfo">Arun Gowtham</span>
</div>
</div>
<span id="47492"></span>
<div id="comment-47492" class="comment not_top_scorer">
<div id="post-47492-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>For high level introduction I recommend to take a look at the following Wiki page: <a href="http://wiki.openstreetmap.org/wiki/Overpass_API/Technical_details">http://wiki.openstreetmap.org/wiki/Overpass_API/Technical_details</a></p>
</div>
<div id="comment-47492-info" class="comment-info">
<span class="comment-age">(13 Jan '16, 14:40)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-47471" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-47471-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

