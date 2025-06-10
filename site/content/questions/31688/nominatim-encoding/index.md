+++
type = "question"
title = "nominatim encoding"
description = '''Hi I&#x27;m consuming the web service of nominatim to reverse geocoding in my .NET Application but the xml I get in my String variable is not the same as I see in the browser and accents the spoils me and makes me strange characters when using coordinates in asia Any idea??? Thanks'''
date = "2014-03-19T15:02:00Z"
lastmod = "2014-03-19T15:58:00Z"
weight = 31688
keywords = [ "nominatim", "encoding" ]
aliases = [ "/questions/31688" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [nominatim encoding](/questions/31688/nominatim-encoding)

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
<span id="post-31688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31688-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-31688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I'm consuming the web service of nominatim to reverse geocoding in my .NET Application but the xml I get in my String variable is not the same as I see in the browser and accents the spoils me and makes me strange characters when using coordinates in asia</p>
<p>Any idea???</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-encoding" rel="tag" title="see questions tagged &#39;encoding&#39;">encoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Mar '14, 15:02</strong></p>
<img src="https://secure.gravatar.com/avatar/2bad034f9416115824ad216468f7878f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kintela&#39;s gravatar image" />
<p><span>kintela</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kintela has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Mar '14, 16:07</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-31688" class="comments-container">
<span id="31691"></span>
<div id="comment-31691" class="comment">
<div id="post-31691-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Could you give some examples (of the code that fails, the data that you're expecting, and the data that you get back)?</p>
</div>
<div id="comment-31691-info" class="comment-info">
<span class="comment-age">(19 Mar '14, 15:11)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="31693"></span>
<div id="comment-31693" class="comment">
<div id="post-31693-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Of course. For example this request <a href="http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=50,9683209807591&amp;lon=2,57099452814137&amp;zoom=18&amp;addressdetails=1">http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=50,9683209807591&amp;lon=2,57099452814137&amp;zoom=18&amp;addressdetails=1</a></p>
<p>The result: D 70, farm, Bettencourt-Rivière, Amiens, Somme, Picardía, Francia metropolitana, 80890, Francia</p>
<p>But in my C# code</p>
<p>public string Inversa(double latitud, double longitud) { WebClient webClient = new WebClient();</p>
<pre><code>        try
        {
&#10;            string cadena = &quot;http://nominatim.openstreetmap.org/reverse?format=xml&amp;lat=&quot; + Convert.ToString(latitud) + &quot;&amp;lon=&quot; + Convert.ToString(longitud) + &quot;&amp;zoom=18&amp;addressdetails=1&quot;;
&#10;            string result = webClient.DownloadString(cadena);
&#10;            return result;
        }
        catch (Exception e)
        {
            throw e;
        }
    }</code></pre>
<p>I get: D 70, farm, Bettencourt-RiviÃ¨re, Amiens, Somme, Picardie, France mÃ©tropolitaine, 80890, France</p>
<p>Thanks</p>
</div>
<div id="comment-31693-info" class="comment-info">
<span class="comment-age">(19 Mar '14, 15:17)</span> <span class="comment-user userinfo">kintela</span>
</div>
</div>
</div>
<div id="comment-tools-31688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31688-form-container" class="comment-form-container">
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

<span id="31697"></span>

<div id="answer-container-31697" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31697-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31697-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31697-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Nominatim always returns its results in UTF-8 encoding. It looks like you are trying to interpret the result using some windows encoding. According to <a href="http://stackoverflow.com/questions/4716470/webclient-downloadstring-returns-string-with-peculiar-characters">this stackoverflow question</a> you need to set <code>webClient.Encoding = System.Text.Encoding.UTF8</code> to enforce the correct encoding.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Mar '14, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-31697" class="comments-container">
<span id="31698"></span>
<div id="comment-31698" class="comment">
<div id="post-31698-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi.</p>
<p>This must be done before using the web client.DownloadString</p>
<p>webClient.Encoding = Encoding.UTF8;</p>
<p>Thanks</p>
</div>
<div id="comment-31698-info" class="comment-info">
<span class="comment-age">(19 Mar '14, 15:58)</span> <span class="comment-user userinfo">kintela</span>
</div>
</div>
</div>
<div id="comment-tools-31697" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31697-form-container" class="comment-form-container">
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

