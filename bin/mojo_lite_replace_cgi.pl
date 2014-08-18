#!/usr/bin/env perl

use Mojolicious::Lite;
use Mojolicious::Plugin::CGI;

any '/hello_world' => sub {
    my ( $self ) = @_;
    $self->render( text => "Bonjour à tous PAS depuis CGI.pm" );
};

# this is now redundant, the above route will take priority
plugin CGI => [ '/hello_world' => "hello_world.cgi" ];

app->start;
