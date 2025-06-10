+++
type = "question"
title = "Calling Nominatim with file_get_contents .."
description = '''I used in a PHP script to call the Nominativ API with file_get_contents. This worked excellently until 13.09.2017. I have tried CURL but no result or error returns. function file_get_contents_curl($cmd, $query) { $level=error_reporting(); error_reporting(E_ALL); $ch = curl_init(); $query= curl_escap...'''
date = "2017-09-23T06:22:00Z"
lastmod = "2018-12-02T11:14:00Z"
weight = 59788
keywords = [ "nominatim", "php", "error" ]
aliases = [ "/questions/59788" ]
osqa_answers = 4
osqa_accepted = true
+++

<div class="headNormal">

# [Calling Nominatim with file_get_contents ..](/questions/59788/calling-nominatim-with-file_get_contents)

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
<span id="post-59788-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59788-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59788-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I used in a PHP script to call the Nominativ API with file<strong><em>_get</em></strong>_contents. This worked excellently until 13.09.2017.</p>
<p>I have tried CURL but no result or error returns.</p>
<pre><code>function file_get_contents_curl($cmd, $query) {
$level=error_reporting();
error_reporting(E_ALL);
$ch = curl_init();
$query= curl_escape($ch,$query);
$url = $cmd.$query;
echo $url.&#39; &lt;--&#39;;
curl_setopt($ch, CURLOPT_AUTOREFERER, TRUE);
curl_setopt($ch, CURLOPT_HEADER, 0);
//Set curl to return the data instead of printing it to the $
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 3);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);       
$data = curl_exec($ch);
curl_close($ch);
error_reporting($level);
return $data;</code></pre>
<p>}</p>
<pre><code>/*result of echo
http://nominatim.openstreetmap.org/search?format=json&amp;limit=1&amp;addressdetails=1%26email%3Dg%40example.com%26street%3D19%2BAhornweg%26city%3DKoenigswinter%26country%3DDeutschland%26postalcode%3D53639
*/</code></pre>
<p>Can anyone help me with a working solution?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-php" rel="tag" title="see questions tagged &#39;php&#39;">php</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Sep '17, 06:22</strong></p>
<img src="https://secure.gravatar.com/avatar/2608aa8e00ed6db4f5d8090f8983fbb8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="user_5359&#39;s gravatar image" />
<p><span>user_5359</span><br />
<span class="score" title="91 reputation points">91</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="user_5359 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Sep '17, 13:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-59788" class="comments-container">
&#10;</div>
<div id="comment-tools-59788" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59788-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="59819"></span>

<div id="answer-container-59819" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59819-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59819-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-59819-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="user_5359 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>PHP's <code>file_get_contents()</code> sends neither HTTP UserAgent nor Referer, which violates the <a href="">usage policy</a> for the server. You can easily add custom HTTP headers by creating an appropriate stream context like that:</p>
<pre><code>// Create a stream
$opts = array(&#39;http&#39;=&gt;array(&#39;header&#39;=&gt;&quot;User-Agent: StevesCleverAddressScript 3.7.6\r\n&quot;));
$context = stream_context_create($opts);
&#10;// Open the file using the HTTP headers set above
$file = file_get_contents(&#39;http://nominatim.openstreetmap.org/search/q=Rome&#39;, false, $context);</code></pre>
<p>For more information see the <a href="http://php.net/manual/en/function.file-get-contents.php">PHP user manual</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Sep '17, 15:58</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-59819" class="comments-container">
&#10;</div>
<div id="comment-tools-59819" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59819-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="59791"></span>

<div id="answer-container-59791" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59791-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59791-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59791-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Do you run the script within the <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> limits, e.g. Number of requests per second? I see the email parameter is a non-existing email. It's possible you got blocked. That would explain why it stopped working from one day to the next.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Sep '17, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-59791" class="comments-container">
<span id="59794"></span>
<div id="comment-59794" class="comment">
<div id="post-59794-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>the email address has been changed for security reasons. If I'm blocked, I would get a corresponding HTML text.</p>
<p>Unfortunately, the code runs on my development machine, but not on the server. In which direction do I have to see which parameters (CURL installation?) can have an effect?</p>
</div>
<div id="comment-59794-info" class="comment-info">
<span class="comment-age">(23 Sep '17, 11:22)</span> <span class="comment-user userinfo">user_5359</span>
</div>
</div>
</div>
<div id="comment-tools-59791" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59791-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65036"></span>

<div id="answer-container-65036" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65036-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65036-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65036-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I had a similar problem while acquiring coordinates for geocoding. I need to add also my email address to url. I combined info from this: <a href="https://gis.stackexchange.com/questions/166006/nominatim-reverse-geocode-gets-blocked-how-do-i-send-a-valid-useragent-or-refe">link text</a> and this: <a href="https://stackoverflow.com/questions/34073169/how-to-header-stream-context-create">link text</a> to get this:</p>
<pre><code>        $url = &#39;https://nominatim.openstreetmap.org/search/&#39;.rawurlencode($location).&#39;?format=json&amp;limit=1&amp;email=youremail@gmail.com&#39;;
&#10;        $data = &#39;&#39;; // empty post
        $opts = array(
            &#39;http&#39; =&gt; array(
            &#39;header&#39; =&gt; &quot;Content-type: text/html\r\nContent-Length: &quot; . strlen($data) . &quot;\r\n&quot;,
            &#39;method&#39; =&gt; &#39;POST&#39;
            ),
        ); 
        // Create a stream
        $context = stream_context_create($opts);
        // Open the file - get the json response using the HTTP headers set above
        $jsonfile = file_get_contents($url, false, $context);
        // decode the json 
        if (!json_decode($jsonfile, TRUE)) {return false;}else{
        //if (empty(array_filter($resp))) {return false;}else{
        $resp = json_decode($jsonfile, true);
        //if(is_string($resp)){$resp = &#39;true&#39;;}else{$resp = &#39;itsnot&#39;;}
        // Extract data (e.g. latitude and longitude) from the results    
        $gps[&#39;latitude&#39;] = $resp[0][&#39;lat&#39;];
        $gps[&#39;longitude&#39;] = $resp[0][&#39;lon&#39;];
        return $gps;}</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Jul '18, 01:21</strong></p>
<img src="https://secure.gravatar.com/avatar/c8925e2f43f3710d1945cff9f7332105?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pablo&#39;s gravatar image" />
<p><span>Pablo</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pablo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65036" class="comments-container">
&#10;</div>
<div id="comment-tools-65036" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65036-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="67034"></span>

<div id="answer-container-67034" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-67034-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-67034-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-67034-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Cool, thanks to lonvia here's a practical example to get around this nonsense with php. Using the browsers <a href="https://stackoverflow.com/questions/10243841/how-to-get-user-agent-in-php">user_agent</a> as a variable.</p>
<pre><code>function OsmAddress() {
    //vars
    $Latitude =&#39;22.56589015&#39;;
    $Longitude =&#39;113.9259518&#39;;
    $USERAGENT = $_SERVER[&#39;HTTP_USER_AGENT&#39;];
&#10;    //main
    $opts = array(&#39;http&#39;=&gt;array(&#39;header&#39;=&gt;&quot;User-Agent: $USERAGENT\r\n&quot;));
    $context = stream_context_create($opts);
    $url4 = file_get_contents(&quot;https://nominatim.openstreetmap.org/reverse?format=json&amp;lat=$Latitude&amp;lon=$Longitude&amp;zoom=18&amp;addressdetails=1&quot;, false, $context);
    $osmaddress = json_decode($url4);  
    $osmaddress1 = $osmaddress-&gt;display_name;
    echo $osmaddress1;
}
OsmAddress();</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Dec '18, 07:35</strong></p>
<img src="https://secure.gravatar.com/avatar/f64caeeb5ed5d7b1626dda1343714f42?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="J0naz&#39;s gravatar image" />
<p><span>J0naz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="J0naz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-67034" class="comments-container">
<span id="67037"></span>
<div id="comment-67037" class="comment">
<div id="post-67037-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So you are re-using/faking the user's useragent for your server-side script to execute a nominatim query on the user's behalf? Not sure if that is a good idea with regards to complying with <a href="https://operations.osmfoundation.org/policies/nominatim/">https://operations.osmfoundation.org/policies/nominatim/</a> . Do not be surprised if your access will be blocked at some point in time. I guess that setting a proper referer, custom user agent (your application's name) a contact email address would be a better way to go.</p>
<p>Note that to get around that "nonsense" you are free (and very welcome) to set up your own nominatim service using our free data.</p>
</div>
<div id="comment-67037-info" class="comment-info">
<span class="comment-age">(02 Dec '18, 11:14)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-67034" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-67034-form-container" class="comment-form-container">
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

