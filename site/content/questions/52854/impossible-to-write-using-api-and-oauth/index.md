+++
type = "question"
title = "impossible to write using API and OAuth"
description = '''Hello, I have build my own OSM server, then I am testing how to modify data on real OSM web sites before doing it on my own server. I followed the russian PHP example available at the end of this page : http://wiki.openstreetmap.org/wiki/OAuth/examples So everything works until I try to write in OSM...'''
date = "2016-11-07T10:30:00Z"
lastmod = "2016-11-07T20:31:00Z"
weight = 52854
keywords = [ "oauth", "put", "api" ]
aliases = [ "/questions/52854" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [impossible to write using API and OAuth](/questions/52854/impossible-to-write-using-api-and-oauth)

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
<span id="post-52854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52854-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I have build my own OSM server, then I am testing how to modify data on real OSM web sites before doing it on my own server.</p>
<p>I followed the russian PHP example available at the end of this page : <a href="http://wiki.openstreetmap.org/wiki/OAuth/examples">http://wiki.openstreetmap.org/wiki/OAuth/examples</a></p>
<p>So everything works until I try to write in OSM web site, neither in the development osm server (<a href="http://api06.dev.openstreetmap.org">http://api06.dev.openstreetmap.org</a>) nor in the production osm server (<a href="http://www.openstreetmap.org">http://www.openstreetmap.org</a>).</p>
<p>Each time I am doing a PUT request, it fails with a '401 Unauthorized' message.</p>
<p>Can somebody help me ?</p>
<p>Here are the PHP code (I write all token variables in include files rather thant using session variables or cookies) :</p>
<p>1) step1.php (requests a user's token, writes it in an include file, then call the authorization url) :</p>
<pre><code>    &lt;?php
    include &#39;parameters.php&#39;;
    try {
        $oauth = new OAuth($consumer_key, $consumer_secret,
                           OAUTH_SIG_METHOD_HMACSHA1, OAUTH_AUTH_TYPE_URI);
        // requiring user&#39;s token
        $future_token_user = $oauth-&gt;getRequestToken($req_url);
        $future_user_token_name = $future_token_user[&#39;oauth_token&#39;];
        $future_user_token_secret = $future_token_user[&#39;oauth_token_secret&#39;];
        // writing user&#39;s token
        $fp = fopen ($include_token_user, &#39;w&#39;);
        fprintf ($fp, &quot;&lt;?php\n%s\n%s\n?&gt;\n&quot;,
                &#39;$oauth_user_token = \&#39;&#39;.$future_user_token_name.&#39;\&#39;;&#39;,
                &#39;$oauth_user_token_secret = \&#39;&#39;.$future_user_token_secret.&#39;\&#39;;&#39;);
        fclose ($fp);
        echo &quot;&lt;a href=\&quot;&quot;.$authurl.&quot;?oauth_token=&quot;.$future_user_token_name.&quot;\&quot;&gt;To authorize&lt;/a&gt;&quot;;
    } catch(OAuthException $E) {
        print_r($E);
    }
    ?&gt;</code></pre>
2) step2.php (executed by the authorization callback url ; starts reading user's token from include file, requests a session token, writes it in another include file, reads user's data ok, writes changeset ko) :
<pre><code>    &lt;?php
    include &#39;parameters.php&#39;;
    include &#39;reading.php&#39;;
    include &#39;writing.php&#39;;
    // reading user&#39;s token
    include $include_token_user;
    // some tests to be consistent
    if(!isset($_GET[&#39;oauth_token&#39;])) {
       echo &quot;No token!&quot;;
       exit;
    }
    $token = $_GET[&#39;oauth_token&#39;];
    if ($token != $oauth_user_token) {
       echo &quot;Authentication error : current token (&quot;.$token
            .&quot;) is not the same as during step1 (&quot;.$oauth_user_token
            .&quot;). Please redo it&quot;;
       exit;
    }
    try {
       $oauth = new OAuth($consumer_key, $consumer_secret,
                          OAUTH_SIG_METHOD_HMACSHA1, OAUTH_AUTH_TYPE_URI);
       $oauth-&gt;enableDebug();
       // using user&#39;s token
       $oauth-&gt;setToken($oauth_user_token, $oauth_user_token_secret);
       // requiring session&#39;s token
       $session_token = $oauth-&gt;getAccessToken($acc_url);
       $session_token_name = strval($session_token[&#39;oauth_token&#39;]);
       $session_token_secret = strval($session_token[&#39;oauth_token_secret&#39;]);
       // using session&#39;s token
       $oauth-&gt;setToken($session_token_name, $session_token_secret);
       // writing session&#39;s token
       $fp = fopen ($include_token_session, &#39;w&#39;);
       fprintf ($fp, &quot;&lt;?php\n%s\n%s\n?&gt;\n&quot;,
                &#39;$oauth_session_token = \&#39;&#39;.$session_token_name.&#39;\&#39;;&#39;,
                &#39;$oauth_session_secret = \&#39;&#39;.$session_token_secret.&#39;\&#39;;&#39;);
       fclose ($fp);
       reading ();
       writing ();
    } catch(OAuthException $E) {
       print_r($E);
    }
    ?&gt;</code></pre>
3) step3.php, made just to demonstrate that we can start from the session's token, but it's the same behaviour as step2.php (reads session's token from include file, reads user's data ok, writes changeset ko) :
<pre><code>    &lt;?php
    include &#39;parameters.php&#39;;
    include &#39;reading.php&#39;;
    include &#39;writing.php&#39;;
    // reading sessions&#39;s token
    include $include_token_session;
    try {
       $oauth = new OAuth($consumer_key, $consumer_secret,
                          OAUTH_SIG_METHOD_HMACSHA1, OAUTH_AUTH_TYPE_URI);
       $oauth-&gt;enableDebug();
       // using session&#39;s token
       $oauth-&gt;setToken($oauth_session_token, $oauth_session_secret);
       reading ();
       writing ();
    } catch(OAuthException $E) {
       print_r($E);
    }
    ?&gt;</code></pre>
4) and all include files :
<p>parameters.php :</p>
<pre><code>    &lt;?php
    $req_url = &#39;http://api06.dev.openstreetmap.org/oauth/request_token&#39;;     // OSM Request Token URL
    $authurl = &#39;http://api06.dev.openstreetmap.org/oauth/authorize&#39;;         // OSM Authorize URL
    $acc_url = &#39;http://api06.dev.openstreetmap.org/oauth/access_token&#39;;      // OSM Access Token URL
    $api_url = &#39;http://api06.dev.openstreetmap.org/api/0.6/&#39;;                // OSM API URL
    // application keys
    $consumer_key = &#39;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&#39;;
    $consumer_secret = &#39;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&#39;;
    // paths to include files
    $include_token_user = &#39;/var/www/html/russian/token_user.php&#39;;
    $include_token_session = &#39;/var/www/html/russian/token_session.php&#39;;
    ?&gt;</code></pre>
reading.php :
<pre><code>    &lt;?php
        function reading () {
       global $oauth, $api_url;
       /// Reading user&#39;s data through /api/0.6/user/details
       $oauth-&gt;fetch($api_url.&quot;user/details&quot;);
       $user_details = $oauth-&gt;getLastResponse();
       // the output response
       echo str_replace(&quot;\n&quot;, &quot;&lt;br/&gt;&quot;,
                        htmlentities($oauth-&gt;getLastResponse())).&quot;&lt;br/&gt;&quot;;
       // parse response, obtain the Osm user&#39;s name and his id
       $xml = simplexml_load_string($user_details);
       echo &quot;&lt;br/&gt;&quot;;
       // Reading user&#39;s preferences
       $oauth-&gt;fetch($api_url.&quot;user/preferences&quot;);
       echo str_replace(&quot;\n&quot;, &quot;&lt;br/&gt;&quot;,
                        htmlentities($oauth-&gt;getLastResponse())).&quot;&lt;br/&gt;&quot;;
    }</code></pre>
writing.php :
<pre><code>    &lt;?php
    function writing () {
       global $oauth, $api_url;
       // writing changeset (with put)
       $changeset = &quot;&lt;?xml version=\&quot;1.0\&quot; encoding=\&quot;UTF-8\&quot;?&gt;&quot;
                   .&quot;&lt;osm version=\&quot;0.6\&quot; generator=\&quot;testrussian\&quot;&gt;&quot;
                   .&quot; &lt;changeset&gt;&quot;
                   .&quot;  &lt;tag k=\&quot;created_by\&quot; v=\&quot;My OSM Service\&quot;/&gt;&quot;
                   .&quot;  &lt;tag k=\&quot;comment\&quot; v=\&quot;Test changeset\&quot;/&gt;&quot;
                   .&quot; &lt;/changeset&gt;&quot;
                   .&quot; &lt;/osm&gt;&quot;;
       $oauth-&gt;fetch($api_url.&quot;changeset/create&quot;, $changeset,
                     OAUTH_HTTP_METHOD_PUT);
       $idchangeset = str_replace(&quot;\n&quot;, &quot;&lt;br/&gt;&quot;,
                                  htmlentities($oauth-&gt;getLastResponse()));
       echo $idchangeset.&quot;&lt;br/&gt;&quot;;
       // Well, close the changer.
       $oauth-&gt;fetch($api_url.&quot;changeset/&quot;.$idchangeset.&quot;/close&quot;, &quot;&quot;,
                     OAUTH_HTTP_METHOD_PUT);
       echo str_replace(&quot;\n&quot;, &quot;&lt;br/&gt;&quot;,
                        htmlentities($oauth-&gt;getLastResponse())).&quot;&lt;br/&gt;&quot;;
    }</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-oauth" rel="tag" title="see questions tagged &#39;oauth&#39;">oauth</span> <span class="post-tag tag-link-put" rel="tag" title="see questions tagged &#39;put&#39;">put</span> <span class="post-tag tag-link-api" rel="tag" title="see questions tagged &#39;api&#39;">api</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Nov '16, 10:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a772c5824347edc161a821dac9334992?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jcj7421&#39;s gravatar image" />
<p><span>jcj7421</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jcj7421 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-52854" class="comments-container">
<span id="52865"></span>
<div id="comment-52865" class="comment">
<div id="post-52865-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Please don't test against the main server!</p>
</div>
<div id="comment-52865-info" class="comment-info">
<span class="comment-age">(07 Nov '16, 19:34)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="52867"></span>
<div id="comment-52867" class="comment">
<div id="post-52867-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello Andy. Of course, I make my tests almost all the time with the test server (api06.dev.openstreetmap.org), but you know, when you use an offical exemple, you follow the documentation but your program fails, and you don't understand why, you will make a lot of tests, including one with the main server, just in case. Regards, JC</p>
</div>
<div id="comment-52867-info" class="comment-info">
<span class="comment-age">(07 Nov '16, 20:31)</span> <span class="comment-user userinfo">jcj7421</span>
</div>
</div>
</div>
<div id="comment-tools-52854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52854-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

