+++
type = "question"
title = "Why doesn&#x27;t Visual Basic WebBrowser control show OSM anymore?"
description = '''Hi everyone! This newbie has an urgent question: I am using the following URL in a Visual Basic (2010) program to show the OSM map in a web browser control. (The VB Webbrowser control uses the settings of the IE on the machine the software runs on.) Me.Map.Navigate(&quot;http://www.openstreetmap.org/?mla...'''
date = "2013-09-25T09:37:00Z"
lastmod = "2013-09-25T11:08:00Z"
weight = 26703
keywords = [ "white", "visualbasic", "empty", "vb2010" ]
aliases = [ "/questions/26703" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Why doesn't Visual Basic WebBrowser control show OSM anymore?](/questions/26703/why-doesnt-visual-basic-webbrowser-control-show-osm-anymore)

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
<span id="post-26703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26703-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everyone!</p>
<p>This newbie has an urgent question: I am using the following URL in a Visual Basic (2010) program to show the OSM map in a web browser control. (The VB Webbrowser control uses the settings of the IE on the machine the software runs on.)</p>
<p>Me.Map.Navigate("http://www.openstreetmap.org/?mlat=" &amp; lat &amp; "&amp;mlon=" &amp; lon &amp; "&amp;zoom=" &amp; level)</p>
<p>Thus, the URL given to the control looks something like this at runtime:</p>
<p><a href="http://www.openstreetmap.org/?mlat=51.9112&amp;mlon=8.1318&amp;zoom=17">http://www.openstreetmap.org/?mlat=51.9112&amp;mlon=8.1318&amp;zoom=17</a></p>
<p>This always worked for the last three years. But strangely, it doesn't work anymore since yesterday(or maybe the day before, I don't know for sure). When I paste the URL into IE, it shows the map as usual, but when my software is told to open the link, it only shows a white page with the OSM Navigation bar on the left and nothing else.</p>
<p>Can anyone help me with this, or at least tell me if anything has been changed in OSM lately? It does look like it, because the above mentioned URL automatically gets changed to the following when opened in a web browser:</p>
<p><a href="http://www.openstreetmap.org/?mlat=51.9112&amp;mlon=8.1318&amp;zoom=17#map=17/51.91120/8.13180">http://www.openstreetmap.org/?mlat=51.9112&amp;mlon=8.1318&amp;zoom=17#map=17/51.91120/8.13180</a></p>
<p>The last part beginning with #map seems to be new to me. But even when I change the URL in my program to the above, extended version, the map won't get shown.</p>
<p>Any help would be very much appreciated, as my software runs on several computers and people start asking me what's wrong.</p>
<p>Thanks,</p>
<p>Dirk.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-white" rel="tag" title="see questions tagged &#39;white&#39;">white</span> <span class="post-tag tag-link-visualbasic" rel="tag" title="see questions tagged &#39;visualbasic&#39;">visualbasic</span> <span class="post-tag tag-link-empty" rel="tag" title="see questions tagged &#39;empty&#39;">empty</span> <span class="post-tag tag-link-vb2010" rel="tag" title="see questions tagged &#39;vb2010&#39;">vb2010</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Sep '13, 09:37</strong></p>
<img src="https://secure.gravatar.com/avatar/4503a7a0d281a017a00814c3e8427cd3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dirk_R&#39;s gravatar image" />
<p><span>Dirk_R</span><br />
<span class="score" title="41 reputation points">41</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dirk_R has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26703" class="comments-container">
<span id="26706"></span>
<div id="comment-26706" class="comment">
<div id="post-26706-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Not sure why your application can't handle the page anymore but this is actually not an <em>extended</em> version but a <em>shorter</em> one: <a href="http://www.openstreetmap.org/#map=17/51.91120/8.13180">http://www.openstreetmap.org/#map=17/51.91120/8.13180</a> (zoom/lat/lon) is now the new format.</p>
</div>
<div id="comment-26706-info" class="comment-info">
<span class="comment-age">(25 Sep '13, 10:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="26709"></span>
<div id="comment-26709" class="comment">
<div id="post-26709-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@scai</span> - not really, the original URL had a marker in it hence the one in the question really was the equivalent (with 2 sets of co-ordinates - one for the marker, one for the map centre).</p>
</div>
<div id="comment-26709-info" class="comment-info">
<span class="comment-age">(25 Sep '13, 10:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="26712"></span>
<div id="comment-26712" class="comment">
<div id="post-26712-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you sure the Webbrowser control uses the settings of IE on the machine the software runs on? I just threw a control on a Windows Form and navigated to the URL in your example and it looks the same as if I switch IE10 to IE7 standards mode.</p>
</div>
<div id="comment-26712-info" class="comment-info">
<span class="comment-age">(25 Sep '13, 10:32)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="26713"></span>
<div id="comment-26713" class="comment">
<div id="post-26713-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@SomeoneElse</span> Oh I missed that, you are right.</p>
</div>
<div id="comment-26713-info" class="comment-info">
<span class="comment-age">(25 Sep '13, 10:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="26714"></span>
<div id="comment-26714" class="comment">
<div id="post-26714-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Hi all and thanks for the fast replies!</p>
<p>EdLoach, you are right! When I turn IE10 back to IE7 settings, that's exactly the picture I get in my program! Only why VB puts the browser element in IE7 mode, I don't know. But I will look into the settings of my project, maybe there's something I overlooked.</p>
<p>Second thing I don't quite get is why this problem only started appearing two days ago. Maybe some of the latest MS security patches?!</p>
<p>Thanks again for your prompt answers!</p>
<p>Dirk</p>
</div>
<div id="comment-26714-info" class="comment-info">
<span class="comment-age">(25 Sep '13, 11:08)</span> <span class="comment-user userinfo">Dirk_R</span>
</div>
</div>
</div>
<div id="comment-tools-26703" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26703-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

