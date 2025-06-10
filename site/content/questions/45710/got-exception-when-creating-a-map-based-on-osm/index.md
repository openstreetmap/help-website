+++
type = "question"
title = "got exception when creating a map based on OSM"
description = '''I would like to run a C# code to create a map based on OSM.  The code is from http://www.codeproject.com/Articles/87944/WPF-Map-Control-using-openstreetmap-org-Data I can build and run the code at Visual Studio 2013. I need to make the map focus on a given lat/lon. So I added   myMap.Focus(); // ena...'''
date = "2015-10-04T23:29:00Z"
lastmod = "2015-10-04T23:35:00Z"
weight = 45710
keywords = [ "c#", "visual-studio", "c#.net" ]
aliases = [ "/questions/45710" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [got exception when creating a map based on OSM](/questions/45710/got-exception-when-creating-a-map-based-on-osm)

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
<span id="post-45710-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-45710-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-45710-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to run a C# code to create a map based on OSM. The code is from <a href="http://www.codeproject.com/Articles/87944/WPF-Map-Control-using-openstreetmap-org-Data">http://www.codeproject.com/Articles/87944/WPF-Map-Control-using-openstreetmap-org-Data</a></p>
<p>I can build and run the code at Visual Studio 2013. I need to make the map focus on a given lat/lon. So I added</p>
<pre><code> myMap.Focus(); // enable manual zoom-in/out 
 myMap.Center(37.806029, -122.407007, 16);</code></pre>
<p>in MainWindow.xaml.cx. I also added</p>
<pre><code>  &lt;map:MapCanvas Latitude=&quot;37.806029&quot; Longitude =&quot;-122.407007&quot; Zoom=&quot;16&quot; x:Name=&quot;myMap&quot;
           /&gt;</code></pre>
<p>in MainWindow.xaml But, when I ran the code, I got exception:</p>
<pre><code>  An exception of type &#39;System.ArgumentOutOfRangeException&#39; occurred in PresentationCore.dll but was not handled in user code
&#10;  Additional information: The parameter value must be greater than zero.</code></pre>
<p>The exception occured at:</p>
<pre><code> public ImageSource CreateImage()
    {
        RenderTargetBitmap bitmap = new RenderTargetBitmap((int)this.**ActualWidth**, (int)this.**ActualHeight**, 96, 96, PixelFormats.Default);
        bitmap.Render(_tilePanel);
        bitmap.Freeze();
        return bitmap;
    }</code></pre>
<p>The "ActualWidth" and "ActualHeight" are all 0s.</p>
<p>How can I set values for them ?</p>
<p>Any help would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-c#" rel="tag" title="see questions tagged &#39;c#&#39;">c#</span> <span class="post-tag tag-link-visual-studio" rel="tag" title="see questions tagged &#39;visual-studio&#39;">visual-studio</span> <span class="post-tag tag-link-c#.net" rel="tag" title="see questions tagged &#39;c#.net&#39;">c#.net</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Oct '15, 23:29</strong></p>
<img src="https://secure.gravatar.com/avatar/b9c47170c54a4fa58922f981df8a54b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="usact&#39;s gravatar image" />
<p><span>usact</span><br />
<span class="score" title="19 reputation points">19</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="usact has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>04 Oct '15, 23:36</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-45710" class="comments-container">
<span id="45711"></span>
<div id="comment-45711" class="comment">
<div id="post-45711-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>debugging of your code and/or some other libraries/examples is not really the scope of this help site for OpenStreetMap, in my opinion</p>
</div>
<div id="comment-45711-info" class="comment-info">
<span class="comment-age">(04 Oct '15, 23:35)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-45710" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-45710-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

