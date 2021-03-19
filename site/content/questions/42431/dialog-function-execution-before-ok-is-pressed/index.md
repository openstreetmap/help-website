+++
type = "question"
title = "Dialog function execution before OK is pressed"
description = '''I am trying to launch a dialog window from an add_button API call. However, the function assigned to the new_dialog executes before I click OK and the code runs through to the function and fails to refresh.  local function reloadAPList()  -- Request new filename from user  new_dialog(&quot;Enter File (wi...'''
date = "2015-05-15T17:34:00Z"
lastmod = "2015-06-29T16:16:00Z"
weight = 42431
keywords = [ "lua", "wireshark" ]
aliases = [ "/questions/42431" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Dialog function execution before OK is pressed](/questions/42431/dialog-function-execution-before-ok-is-pressed)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-42431-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-42431-score" class="post-score" title="current number of votes">0</div><span id="post-42431-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I am trying to launch a dialog window from an <code>add_button</code> API call. However, the function assigned to the new_dialog executes before I click OK and the code runs through to the function and fails to refresh.</p><pre><code>   local function reloadAPList()
      -- Request new filename from user
      new_dialog(&quot;Enter File (without extension)&quot;,
                 function (basename) filename = basename end,
                 &quot;Filename&quot;)

      message(&quot;Opening file: &quot; .. filename)
      local csv_file = assert(io.open(filename, &quot;r&quot;))

      if csv_file==nil then
          warn(err)
          return
      end

      -- Read CSV line
      local line = csv_file:read()

      -- Flush out old table contents
      for k,v in pairs(apList) do
         apList[k] = nil
      end

      -- Build AP Object Name List table
      apList = fromCSV(line)
   end

   aw:add_button(&quot;Reload&quot;, reloadAPList )</code></pre><p>If I click the reload button again I can see that it attempts to open the file matching the string I passed in on the previous attempt.</p><p>Any ideas why it does not take the filename I pass in the first time round?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-lua" rel="tag" title="see questions tagged &#39;lua&#39;">lua</span> <span class="post-tag tag-link-wireshark" rel="tag" title="see questions tagged &#39;wireshark&#39;">wireshark</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '15, 17:34</strong></p><img src="https://secure.gravatar.com/avatar/8e191d3ad5ed97a4ab999dfe6087ae92?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="carlwain74&#39;s gravatar image" /><p><span>carlwain74</span><br />
<span class="score" title="1 reputation points">1</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="carlwain74 has no accepted answers">0%</span></p></div></div><div id="comments-container-42431" class="comments-container"><span id="42456"></span><div id="comment-42456" class="comment"><div id="post-42456-score" class="comment-score"></div><div class="comment-text"><p>I guess, we would need more of your code to recreate the problem.</p></div><div id="comment-42456-info" class="comment-info"><span class="comment-age">(17 May '15, 06:14)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42477"></span><div id="comment-42477" class="comment"><div id="post-42477-score" class="comment-score"></div><div class="comment-text"><p>Essentially all you need to do is invoke a new dialog from within a button function. You can see above that aw:add_button calls reloadApList when the button is clicked. In reloadApList I call new_dialog with an inline function to assign the string to a local variable (not shown in code snippet).</p><p>The dialog box launches, but the message call after the new_dialog prints the filename from the previous button click.</p><p>I hope that helps..</p></div><div id="comment-42477-info" class="comment-info"><span class="comment-age">(17 May '15, 20:55)</span> <span class="comment-user userinfo">carlwain74</span></div></div><span id="42479"></span><div id="comment-42479" class="comment"><div id="post-42479-score" class="comment-score"></div><div class="comment-text"><p>can you please test the following code and post the output of message() here?</p><pre><code>   local function reloadAPList()

   local filename = &quot;_notset_&quot;

   local function assign_filename(basename)
      message(&quot;Filename before:&quot; .. filename)
      filename = basename
      message(&quot;Filename after:&quot; .. filename)
   end

      -- Request new filename from user
      new_dialog(&quot;Enter File (without extension)&quot;, assign_filename, &quot;Filename&quot;)

      message(&quot;Opening file: &quot; .. filename)</code></pre></div><div id="comment-42479-info" class="comment-info"><span class="comment-age">(17 May '15, 21:42)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div><span id="42501"></span><div id="comment-42501" class="comment"><div id="post-42501-score" class="comment-score"></div><div class="comment-text"><p>This is the output in the console</p><pre><code>5/18/2015 8:16:05 AM MESSAGE: Opening file: c:\temp\AP_Batch.csv
5/18/2015 8:16:34 AM MESSAGE: Filename before:c:\temp\AP_Batch.csv
5/18/2015 8:16:34 AM MESSAGE: Filename after:test.csv</code></pre><p>The first log entry appeared when I clicked the button. The second and third appeared after I entered a string and clicked OK.</p><p>Note that test.csv does not exist and I was expecting the assert on io.open to detect that.</p></div><div id="comment-42501-info" class="comment-info"><span class="comment-age">(18 May '15, 08:19)</span> <span class="comment-user userinfo">carlwain74</span></div></div><span id="42502"></span><div id="comment-42502" class="comment"><div id="post-42502-score" class="comment-score"></div><div class="comment-text"><p>The assert came when I clicked the button for a second time. It looks like the code after the new_dialog executes before the dialog is closed.</p></div><div id="comment-42502-info" class="comment-info"><span class="comment-age">(18 May '15, 08:30)</span> <span class="comment-user userinfo">carlwain74</span></div></div><span id="42505"></span><div id="comment-42505" class="comment not_top_scorer"><div id="post-42505-score" class="comment-score"></div><div class="comment-text"><p>strange thing... please file a bug report at <a href="https://bugs.wireshark.org">https://bugs.wireshark.org</a></p></div><div id="comment-42505-info" class="comment-info"><span class="comment-age">(18 May '15, 08:46)</span> <span class="comment-user userinfo">Kurt Knochner ♦</span></div></div></div><div id="comment-tools-42431" class="comment-tools"><span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a></div><div class="clear"></div><div id="comment-42431-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="43689"></span>

<div id="answer-container-43689" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-43689-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-43689-score" class="post-score" title="current number of votes">0</div><span id="post-43689-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>I don't think this is a bug. The <code>new_dialog()</code> function is non-blocking, creating a non-modal dialog window. So in the question's script it's creating the dialog window but immediately returning to process more of the Lua code, as it should.</p><p>I think the right way to code this in Lua is to put the rest of the logic that is currently after <code>new_dialog()</code> into the callback function assigned by <code>new_dialog()</code>. In other words, this:</p><pre><code>local function reloadAPList(basename)
    filename = basename

    message(&quot;Opening file: &quot; .. filename)
    local csv_file = assert(io.open(filename, &quot;r&quot;))

    if csv_file==nil then
        warn(err)
        return
    end

    -- Read CSV line
    local line = csv_file:read()

    -- Flush out old table contents
    for k,v in pairs(apList) do
        apList[k] = nil
    end

    -- Build AP Object Name List table
    apList = fromCSV(line)
end

local function get_filename()
    -- Request new filename from user
    new_dialog(&quot;Enter File (without extension)&quot;,
               reloadAPList,
               &quot;Filename&quot;)
end

aw:add_button(&quot;Reload&quot;, get_filename )</code></pre></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>29 Jun '15, 16:16</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p><span>Hadriel</span><br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div></div><div id="comments-container-43689" class="comments-container"></div><div id="comment-tools-43689" class="comment-tools"></div><div class="clear"></div><div id="comment-43689-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

