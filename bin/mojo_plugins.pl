#!perl

use strict;
use warnings;
use feature qw/ say /;

use MetaCPAN::Client;

my $mcpan = MetaCPAN::Client->new;
my $rs    = $mcpan->module( {
	all => [
		{ 'module.name' => 'Mojolicious::Plugin::*' },
		{ "status" => "latest" },
	],
} );

my ( @plugins,@passed,@failed );

while ( my $module = $rs->next ) {
	push( @plugins,$module->data->{module}[0]{name} );
}

say scalar( @plugins ) . " Mojolicious plugin modules found...";
say "Installing latest Mojolicious...";

system( "perl","-V" );
system( "cpanm","Mojolicious" );

foreach my $plugin ( @plugins ) {

	system( "cpanm","--reinstall",$plugin );

	if ( $? ) {
		push( @failed,$plugin );
	} else {
		push( @passed,$plugin );
	}
}

say "---------------------";
say scalar( @passed ) . " plugins installed clean";
say scalar( @failed ) . " plugins failed to install";

__END__
---------------------
255 plugins installed clean
63 plugins failed to install (25%, approx 5% due to incompat with latest Mojolicious)
